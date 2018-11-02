"""non greedy method"""

import re

x = ('From: Using the : characters')
y = re.findall('^F.+?:', x)

print(y)
