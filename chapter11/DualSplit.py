"""Take certain things after a space"""

import re

# without regular expression
line = ('From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008')

words = line.split()
email = words[1]
pieces = email.split('@')

print(pieces)

# with regular expression

y = re.findall('@([^ ]*)', line)
print(y)

y = re.findall('^From .*@([^ ]*)', line)
print(y)
