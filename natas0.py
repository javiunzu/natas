"""
Help script to resolve natas challenge #0
"""
import requests
import json

level = 'natas0'
url = 'http://{}.natas.labs.overthewire.org'.format(level)

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
Just inspect the source.
"""
response = requests.get(url, auth=auth)
print(response.text)
