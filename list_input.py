"""user input in list"""

size = int(input('Enter the size of the list:'))

lst = [0] * size

print('Enter the numbers:')
for i in range(size):
    lst[i] = int(input())

print(lst)
