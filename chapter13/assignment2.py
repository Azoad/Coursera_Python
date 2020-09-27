"""
Read JSON
"""

import json
import urllib.request
import urllib.parse
import urllib.error

js = input('Enter Location: ')


url = urllib.request.urlopen(js)
raw_data = url.read()
data = json.loads(raw_data)
c_data = data["comments"]
print('Count: ', len(c_data))

total = 0
for c in c_data:
    m = int(c['count'])
    total = m + total

print('Sum: ', total)
