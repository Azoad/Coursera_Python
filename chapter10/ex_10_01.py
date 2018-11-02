"""Find most commits using tupple"""

fname = input('Enter a file name: ')
fhand = open(fname)

counts = dict()
for line in fhand:
    if not line.startswith('From '):
        continue
    line = line.split()
    line = line[1]
    counts[line] = counts.get(line, 0) + 1
print(counts)

lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)
for key, val in lst[:1]:
    print(val, key)
