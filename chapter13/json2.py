"""
Loop through json
"""

import json

data = '''
[
	{
		"id" : "001",
		"x" : "2",
		"name" : "Chuck"
	},
	{
		"id" : "009",
		"x" : "7",
		"name" : "Brent"
	}
]'''

info = json.loads(data)
print('User Count: ', len(info))

for info in info:
    print('Name: ', info['name'])
    print('Id: ', info['id'])
    print('Attribute: ', info['x'])
