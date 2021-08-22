import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Location: ')
parms = dict()
parms['url'] = url
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
value = tree.findall('.//count')
sum = 0
count = 0
for item in value:
    sum += (int(item.text))
    count += 1
print("Count: ", count)
print("Sum", sum)






