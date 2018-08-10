"""Gimme A Break"""

COUNT = 0
TOT = 0.0

while True:
    SVAL = input('Enter a number: ')
    if SVAL == 'done':
        break
    try:
        FVAL = float(SVAL)
    except:
    	print('Invalid input')
    	continue
    # print(FVAL)
    COUNT = COUNT + 1
    TOT = TOT +FVAL

# print('ALL DONE')
print(TOT, COUNT, TOT / COUNT)
