"""looks for the biggest match"""

import re

x = ('From: Using the : character')
y = re.findall('^F.+:', x)
print(y)
