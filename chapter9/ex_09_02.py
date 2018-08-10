"""Read from mails and shows days and mails"""

fname = input('Enter a file name: ')
fhand = open(fname)

ldays = list()
ddays = dict()
for line in fhand:
    if not line.startswith('From '):
        continue
    words = line.split()
    ldays.append(words[2])

for day in ldays:
    if day not in ddays:
        ddays[day] = 1
    else:
        ddays[day] += 1

print(ddays)
