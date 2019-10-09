"""
go to a site, check all the anchored sites
grab a count and position
retrieve for that position
do the same
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

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

print('Retrieving: ', url)

for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    l = []

    for tags in tags:
        l.append(tags.get('href', None))

    print('Retrieving: ', l[position - 1])
    url = l[position - 1]
