"""looping through a set"""

print('Before')
for thing in [9, 41, 12, 3, 74, 15]:
    print(thing)
print('After')


# find the largest number

LARGEST_SO_FAR = -1
print('Before', LARGEST_SO_FAR)

for the_num in [9, 41, 12, 3, 74, 15]:

    if the_num > LARGEST_SO_FAR:
    
        LARGEST_SO_FAR = the_num
    
    print('largest_so_far', LARGEST_SO_FAR,
          'current number', the_num)
	
print('After', LARGEST_SO_FAR)		

# finding the largest using None

LARGEST_SO_FAR = None
print('Before', LARGEST_SO_FAR)

for the_num in [9, 41, 12, 3, 74, 15]:

    if LARGEST_SO_FAR is None:
        LARGEST_SO_FAR = the_num
        
    elif the_num > LARGEST_SO_FAR:
        LARGEST_SO_FAR = the_num
    
    print('LARGEST_SO_FAR', LARGEST_SO_FAR,
          'current number', the_num)
    
print('After', LARGEST_SO_FAR)  
