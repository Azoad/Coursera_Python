"""
Use regular expression to find all the links
"""

import urllib.request
import urllib.parse
import urllib.error
import re

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
links = re.findall(b'href="(http://.*?)"', html)
for link in links:
    print(link.decode())
