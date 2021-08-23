import urllib.request, urllib.parse, urllib.error
import json
import ssl

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
for user in js['comments']:
    num += 1
    total += user['count']

print("Count: ", total)
print("Sum: ", num)