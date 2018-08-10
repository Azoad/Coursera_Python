"""Parsing and Extracting"""

DATA = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

ATPOS = DATA.find('@')
print('Position of @ is:', ATPOS)

SPPOS = DATA.find(' ', ATPOS)
print('Position of space after the mail is:', SPPOS)

HOST = DATA[ATPOS+1:SPPOS]
print('The host of the mail is:', HOST)
