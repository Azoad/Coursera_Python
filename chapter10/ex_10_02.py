"""Find most hours"""

fname = input('Enter a file name: ')
fhand = open(fname)

counts = dict()
for line in fhand:
    if not line.startswith('From '):
        continue
    line = line.split()
    line = line[5]
    line = line.split(':')
    line = line[0]
    counts[line] = counts.get(line, 0) + 1
print(counts)

hourlist = list()
for hour, count in counts.items():
    hourlist.append((hour, count))

hourlist.sort()
for hour, count in hourlist:
    print(hour, count)
