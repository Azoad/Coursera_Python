hrs = input('Enter Hours: ')
try:
    fhrs = float(hrs)
except:
    fhrs = -1
if fhrs < 0	:
    print('Error, please enter numeric input')
else:
    rate = input('Enter Rate: ')
    try:
        frate = float(rate)
    except:
        frate = -1
    if frate < 0:
        print('Error, please enter numeric input')
    else:
        if fhrs > 40:
            xhrs = fhrs - 40
            ppay = 40 * frate
            xpay = 1.5 * xhrs * frate
            print('Pay:', ppay + xpay)
        else:
            print('Pay:', fhrs * frate) 