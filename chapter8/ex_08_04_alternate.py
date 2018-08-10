fname = input("Enter file name: ")
fh = open(fname)
words = list()
for line in fh:
    words = words + line.split()
    words.sort()
list = []

for word in words:
	if word not in list:
		list.append(word)
print(list) 