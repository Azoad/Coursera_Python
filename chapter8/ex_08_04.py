fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
	print(line.split())
	word = line.split()
	print('----------------------------------')
	print(word)
	if word in lst:
		continue
	else:
		lst = lst + word
print('-------------------------------------')
print(lst)
print('-------------------------------------')
print(sorted(lst))
print('-------------------------------------')
set = set(lst)
res = list(set)
print(sorted(res))