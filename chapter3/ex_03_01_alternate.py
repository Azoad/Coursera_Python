hrs = input('Enter Hours: ')
rate = input('Enter Rate: ')
fhrs = float(hrs)
frate = float(rate)
if  fhrs > 40 :
	ppay = fhrs * frate
	xpay = (fhrs - 40) * (frate * .5)
	pay = ppay + xpay
else :
	pay = fhrs * frate
print('Pay:',pay)	