"""
read a file
find the numbers
sum the numbers
"""
import re

hand = open('E:/Coursera/py4e/files/regex_sum_94852.txt')

lines = list()
sentence = ""

for line in hand:
    lines.append(line.strip())
    sentence += line

num = re.findall('[0-9]+', sentence)
num = list(map(int, num))

# print(len(num))
print(sum(num))
