"""pattern search"""
import re

hand = open('E:/Coursera/py4e/files/mbox-short.txt')
count = 0
for line in hand:
    line = line.rstrip()
    lst = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line)
    if len(lst) > 0:
        print(lst)
        count += 1
print(count)
