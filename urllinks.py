# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Adenn.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
count = 7
position = 18
tags_lst = []

for x in range(count):
    tags = soup('a')
    my_tags = tags[position - 1]
    needed_tag = my_tags.get('href', None)
    tags_lst.append(needed_tag)
    url = str(needed_tag)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
for name in tags_lst:
    print(name)


