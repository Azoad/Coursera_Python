import random

# random generates random number
# between 0,1 and not include 1
for i in range (10):
	x =  random.random()
	print(x)

# randint() takes 2 numbers high and low
# then returns a random integer between them
y = random.randint(0,10)
print(y)	