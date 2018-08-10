numlist = list()

while (True) :
	inp = input('Enter a number: ')

	if inp == 'done' :
		break

	value = float(inp)
	numlist.append(value)

maximum = max(numlist)
minimum = min(numlist)

print(numlist)
print('Max:',maximum)
print('Min:',minimum)		