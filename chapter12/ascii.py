"""
ASCII value check
"""
print('ASCII value of H is:', ord('H'))
print('ASCII value of 1 is:', ord('1'))
print('ASCII value of \\n is:', ord('\n'))
if (ord('H') + ord('i')) < (ord('z') + ord('z') + ord('z')):
    print('Hi is lower than zzz')
else:
    print('zzz is lower than Hi')
