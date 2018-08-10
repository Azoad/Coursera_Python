hrs = input('Enter Hours: ')
rate = input('Enter Rate: ')

fhrs = float(hrs)
frate = float(rate)

def computepay(h,r) :

	if  fhrs > 40 :
		ppay = fhrs * frate
		xpay = (fhrs - 40) * (frate * .5)
		pay = ppay + xpay
		return pay
	else :
		pay = fhrs * frate
		return pay

ppay = computepay(fhrs,frate)
print('Pay:',ppay)	