"""using get"""
fname = input('Enter file name: ')
try:
    fhandle = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
mail = dict()
for line in fhandle:
    if line.startswith('From '):
        line = line.split()
        count = line[1]
        mail[count] = mail.get(count, 0) + 1
print(mail)
