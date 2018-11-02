"""searching using regular expression find()"""
import re

hand = open('E:/Coursera/py4e/files/mbox-short.txt')
count = 0
for line in hand:
    line = line.rstrip()
    if line.find('From: ') >= 0:
        print(line)
        count = count + 1
print(count)
