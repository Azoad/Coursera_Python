"""Take a file as input and display it at uppercase"""
fname = input('Enter the file name: ')
try:
	file = open(fname)
except:
	print('Error in file!')
	quit() 
for line in file:
    print(line.strip().upper())
