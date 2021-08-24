import urllib.request, urllib.parse
import json

api_key = 42
serviceurl = "http://py4e-data.dr-chuck.net/json?"

while True:

    address = input("Enter location: ")

    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)

    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrived', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    placeid = js["results"][0]['place_id']
    print("Place id", placeid)
