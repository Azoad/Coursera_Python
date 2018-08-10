"""Take a file from user find a string count them find num in those show average"""
fname = input('Enter the file name: ')
try:
	file = open(fname)
except:
	print('Error in file!')
	quit()
count = 0
res = 0
for line in file:
	if line.startswith('X-DSPAM-Confidence:'):
		spos = line.find(':')
		num = line[spos+2:]
		res = res + float(num)
		print(line.strip())
		print(num.strip())	
		print('Result after addition:', res, '\n')	
		count = count + 1
	
print("Average spam confidemnce:", (res/count))
