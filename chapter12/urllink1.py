"""
go to a site, check all the anchored sites
"""

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
print(tags, '\n')
for tags in tags:
    print(tags.get('href', None))
