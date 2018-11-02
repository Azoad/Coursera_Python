"""
	search for lines starts with X
	followed by non whitespace characters and ':'
	followed by a space and any number
	may be decimal
"""

import re

hand = open('E:/Coursera/py4e/files/mbox-short.txt')
count = 0
for line in hand:
    line = line.rstrip()
    if re.search('^X\S*: [0-9]+', line):
        count += 1
        print(line)
print(count)
