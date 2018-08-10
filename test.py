print('this is the first one:')
print('let\'s do this!')
print('add 5 and -3')
f = 5
t = -3
print('addition of',str(f),'and',str(t),'is :',str(f+t))

print('-----------------------------')
print('this is the second one:')
x = 'It is not America but it is Bangladesh'
lens = len(x)
print('Length of \'' +x+ '\' is : '+str(lens))

print('------------------------------')
print('this is the third one:')
a = 5
if a<10:
	print('Smaller!')
if a>20:
	print('Larger!')
print('Finish')

print('------------------------------')
print('this is the fourth one:')
n = 5
while n>0:
    print(n)
    n = n-1
print('Blastoff!')    

print('------------------------------')
print('this is the fifth one:')
hrs = input("Enter Hours:")
fhrs = float(hrs)
rate = input("Enter rate:")
frate = float(rate)
pay = fhrs*frate
spay = str(pay)
print("Pay:",spay)

print('------------------------------')
print('this is the sixth one:')
print('Multiplication table:')
num = input('Enter a number:')
for n in range (1,11):
	print(str(num)+' X '+str(n)+' =',int(n)*int(num)) 

print('------------------------------')
print('this is the seventh one:')    
x = 5
if x > 2:
    print('Bigger than 2')
    print('Still bigger')
print('Done with 2')
for i in range(5):
    print(i)
    if i > 2:
        print('Bigger than 2')
    print('Done with i',i)
print('All done')
print('------------------------------')
print('this is the eighth one:')
x = 15
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
elif x < 20 :
    print('Big')
elif x < 40 :
    print('Large')
elif x < 100 :
    print('Huge')
else :
    print('Ginormous')

print('------------------------------')
print('this is the ninth one:')
x = input('Enter a positive number : ')
try :
    ix = int(x)
except :
    ix = -1
print('The value is ',ix)
if ix > 0 :
    print('Number')
else :
    print('Not a number')
	