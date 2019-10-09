"""
I have no clue
"""

import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET

xml = input('Enter location: ')
print('Retrieving ', xml)
url = urllib.request.urlopen(xml)
data = url.read()

print('Retrieved ', len(data), 'characters')

tree = ET.fromstring(data)
counts = tree.findall('.//count')
print('Count: ', len(counts))
total = 0

for count in counts:
    i = int(count.text)
    total = i + total
print('Sum: ', total)

# commentinfo = ET.fromstring(data)
# lst = commentinfo.findall('comments/comment/count')
# print('Count: ', len(lst))

# sum = 0
# for count in lst:
#     i = int(count.text)
#     sum = sum + i
# print('Sum: ', sum)
