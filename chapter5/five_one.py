"""Errorless Naming Infinite loop"""
N = 5
while N > 0:
    print(N)
    N = N - 1
print('Blastoff!')
print(N)

while True:
    LINE = input('> ')
    if LINE[0] == '#':
        continue
    if LINE == 'done':
        break
    print(LINE)
print('Done!')
