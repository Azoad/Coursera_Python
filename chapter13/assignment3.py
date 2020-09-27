"""
Use API to return place ID
"""

import urllib.request
import urllib.error
import urllib.parse
import json

api_key = 42
s_url = 'http://py4e-data.dr-chuck.net/json?'

address = input('Enter location: ')

parms = dict()
parms['address'] = address
parms['key'] = api_key
url = s_url + urllib.parse.urlencode(parms)
print('Retrieving ', url)

uurl = urllib.request.urlopen(url)
r_data = uurl.read()
print('Retrieved ', len(r_data), ' characters')

data = json.loads(r_data)
print('Place id ', data['results'][0]['place_id'])
