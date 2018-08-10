"""finding maximum and minimum"""

LARGEST = None
SMALLEST = None

while True:
    NUM = input("Enter a number: ")
    if NUM == 'done':
        break
    try:
        F = float(NUM)
    except:
        print('Invalid input')
        continue

    if SMALLEST is None:
        SMALLEST = F
    elif SMALLEST > F:
        SMALLEST = F
    if LARGEST is None:
        LARGEST = F
    elif F > LARGEST:
        LARGEST = F

print('Maximum is', int(LARGEST))
print('Minimum is', int(SMALLEST))
