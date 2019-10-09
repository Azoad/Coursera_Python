"""
Scraping Numbers from HTML using BeautifulSoup
"""

from urllib.request import urlopen
import ssl
from bs4 import BeautifulSoup


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the contents of span tags

tags = soup('span')
sum = 0
count = 0
for tag in tags:
    # convert values into integer

    i = int(tag.contents[0])
    sum = sum + i
    count = count + 1

print('Count ', count)
print('Sum ', sum)
