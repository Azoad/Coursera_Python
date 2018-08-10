"""Read a file and find top 10 most common words"""

fhand = open("E:/Coursera/py4e/files/romeo.txt")

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
# print(lst)

lst = sorted(lst, reverse=True)
for val, key in lst[:10]:
    print(key, val)

# the whole work of the two loops can be done in only one line

#print(sorted([(v, k) for k, v in counts.items()], reverse=True))
