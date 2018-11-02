"""Starts with From have @"""

import re

hand = open('E:/Coursera/py4e/files/mbox-short.txt')
count = 0

for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line):
        print(line)
        count = count + 1

print(count)
