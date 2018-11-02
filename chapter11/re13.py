""""""

import re

hand = open('E:/Coursera/py4e/files/mbox-short.txt')

for line in hand:
    line = line.rstrip()

    x = re.findall('^From .* ([0-9][0-9]):', line)

    if len(x) > 0:
        print(x)
