"""
Help script to resolve natas challenge #2
"""
import requests
import json

level = 'natas2'
url = 'http://{}.natas.labs.overthewire.org'.format(level)

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
Same as first level. Right clicking has been deactivated. Only a problem for GUI users ;)
"""
response = requests.get(url, auth=auth)
print(response.text)
