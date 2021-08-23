import json
import ssl
import urllib.error
import urllib.parse
import urllib.request

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter Location: ')
url = "http://py4e-data.dr-chuck.net/comments_42.json"
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieving', url)
print('Retrieved', len(data), 'characters')
js = json.loads(data)

num = 0
total = 0
for _ in js:
    num += int(js['comments'][0]['count'])
    print(num)
    total += 1
print(js)
print("Count: ", total)
print("Sum: ", num)
