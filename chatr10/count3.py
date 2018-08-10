import string

fhand = open('E:/Coursera/py4e/files/romeo-full.txt')

counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()

    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

lst = list()
for key, value in list(counts.items()):
    lst.append((value, key))

lst.sort(reverse=True)

for key, value in lst[:10]:
    print(key, value)
