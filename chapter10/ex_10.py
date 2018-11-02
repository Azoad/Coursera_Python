"""Worked exercise"""

fname = input('Enter file: ')
if len(fname) < 1:
    fname = 'E:/Coursera/py4e/files/clown.txt'

fhand = open(fname)

di = dict()
for line in fhand:
    line = line.strip()
    words = line.split()
    for word in words:
        di[word] = di.get(word, 0) + 1

# print(di)

temp = list()

for k, v in di.items():
    # print(k, v)
    newt = (v, k)
    temp.append(newt)

print('Flipped', temp)

temp = sorted(temp, reverse=True)
print('Sorted', temp[:5])

for v, k in temp[:5]:
    print(k, v)
