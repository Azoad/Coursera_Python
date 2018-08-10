"""docstring"""
N = input('Enter score: ')
try:
    F = float(N)
except GiveTypeNameHere:
    F = -1

def computegrade(num):
    """to compute grade"""
    if num < 0:
        print('Bad score')
    else:
        if num > 1:
            print('Bad score')
        elif num >= 0.9:
            print('A')
        elif num >= 0.8:
            print('B')
        elif num >= 0.7:
            print('C')
        elif num >= 0.6:
            print('D')
        elif num < 0.6:
            print('F')
        else:
            print('Bad score')        

computegrade(F)            
