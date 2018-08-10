hrs = input('Enter Hours: ')
rate = input('Enter Rate: ')
fhrs = float(hrs)
frate = float(rate)
if  fhrs > 40 :
	xhrs = fhrs - 40
	ppay = 40 * frate
	xpay = 1.5 * xhrs * frate 
	print('Pay:',ppay+xpay)
else :	
	print('Pay:',fhrs*frate)