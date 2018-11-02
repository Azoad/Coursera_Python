"""input regular expression and count"""

import re

hand = open('E:/Coursera/py4e/files/mbox.txt')

n = input('Enter a regular expression:')
count = 0
for line in hand:
    line = line.rstrip()

    x = re.findall(str(n) + '', line)
    if len(x) > 0:
        count += 1

print('mbox.txt had ', count, 'lines that matched', n)
