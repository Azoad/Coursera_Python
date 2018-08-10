"""find the number and convert it to floating point"""

str = "X-DSPAM-Confidence:    0.8475";

ipos = str.find(':')
piece = str[ipos+2:]
value = float(piece)

print(value)
