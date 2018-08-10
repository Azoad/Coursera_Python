"""find the number and convert it to floating point"""

text = "X-DSPAM-Confidence:    0.8475";

sfind = text.find(' ')
num = text[sfind+1:]
fnum = float(num)
print(fnum) 
