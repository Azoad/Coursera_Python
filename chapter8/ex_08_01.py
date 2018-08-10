"""Take a list
	define a function 
	chop to remove first and last element
	middle to show all but first and last element"""
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def chop(list):
	del list[0]
	del list[-1]
	return None

def middle(list):
		middle = list[1:-1]
		return middle

print(chop(list))
new_list = middle(list)
print(new_list)			
