fhan = open('mbox-short.txt')

for line in fhan:
	line = line.rstrip()
	#print('Line:', line)
	words = line.split()
	#print('Words', words)

	"""Guardian pattern
	if len(words) < 1 :
		continue
	if line == '':
		print('Skip')
		continue	
	if words[0] != 'From' :
		print('Ignore')
		continue """
	
	if len(words) < 3 or words[0] != 'From' :
		continue

	print(words[2])	
