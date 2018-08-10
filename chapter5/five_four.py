"""counting in a loop"""

COUNT = 0
print('Before', COUNT)

for thing in [9, 41, 12, 3, 74, 15]:
    
    COUNT = COUNT + 1
    print('counter value:', COUNT,
          '\tcurrent value:', thing)

print('After', COUNT)

# add all values

COUNT = 0
print('Before', COUNT)

for thing in [9, 41, 12, 3, 74, 15]:
    
    COUNT = COUNT + thing
    print('current value:', thing,
          '\tcounter value:', COUNT)

print('After', COUNT)

# find average value


COUNT = 0
SUM = 0
print('Before', COUNT)

for thing in [9, 41, 12, 3, 74, 15]:
    
    COUNT = COUNT + 1
    SUM = SUM + thing
    print('counter value:', COUNT,
          '\tsummation:', SUM,
          '\taverage value:', 
          round(SUM / COUNT))

print('After', COUNT, SUM, 
      round(SUM / COUNT))

# filtering in a loop

print('Before')

for value in [9, 41, 12, 3, 74, 15]:

    if value > 20:
        print(value, 'is larger than 20')

print('After')

# search using a boolean variable

FOUND = False
print('Before', FOUND)

for value in [9, 41, 12, 3, 74, 15]:

    if value == 3:
        FOUND = True
    print(FOUND, value)

print('After', FOUND)

# finding the smallest

SMALLEST_SO_FAR = None
print('Before', SMALLEST_SO_FAR)

for the_num in [9, 41, 12, 3, 74, 15]:

    if SMALLEST_SO_FAR is None:
        SMALLEST_SO_FAR = the_num
        
    elif the_num < SMALLEST_SO_FAR:
        SMALLEST_SO_FAR = the_num
    
    print('SMALLEST_SO_FAR', SMALLEST_SO_FAR,
          'current number', the_num)
    
print('After', SMALLEST_SO_FAR)  
