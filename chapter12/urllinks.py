"""
go to a site, check all the anchored sites
"""

import urllib.request
import urllib.parse
import urllib.error
import ssl
from bs4 import BeautifulSoup


# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tags in tags:
    print(tags.get('href', None))
