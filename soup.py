# File reads a url :  http://py4e-data.dr-chuck.net/comments_1276630.html
# And sums up the values in the span tag "Contents: "

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the spans
spans = soup('span')
total = 0
for nums in spans:
    # Look at the parts of a span and put index 0 in num
    num = int(nums.contents[0])
    total += num
print(total)

