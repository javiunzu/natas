"""
Help script to resolve natas challenge #8
"""
import requests
import json
import binascii
import base64

level = 'natas8'
url = 'http://{}.natas.labs.overthewire.org'.format(level)

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
In the source code there is an encoded secret. If we decode it we have the
value we have to send to the form.
Decoding it is just perform the reverse operations of the ones used for
encoding.
"""
encoded = b'3d3d516343746d4d6d6c315669563362'
decoded = base64.b64decode(binascii.unhexlify(encoded)[::-1])
response = requests.post(url, auth=auth, data={'secret': decoded, 'submit': 'submit'})
print(response.text)
