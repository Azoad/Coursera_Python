"""Who sent the most mails"""

fname = input('Enter a file name: ')
fhand = open(fname)

lmails = list()
dmails = dict()
for line in fhand:
    if not line.startswith('From '):
        continue
    words = line.split()
    lmails.append(words[1])

for count in lmails:
    if count not in dmails:
        dmails[count] = 1
    else:
        dmails[count] += 1

name = list()
maximum = 0
count = 0

for key in dmails:
    name.append(key)
    if dmails[key] > maximum:
        maximum = dmails[key]
        count += 1

print(name[count], maximum)
