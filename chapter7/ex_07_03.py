"""just for fun"""
fname = input('Enter the file name: ') #pylint: disable=C0103

try:
    if fname == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punk\'d!')
    else:
        file_handler = open(fname) #pylint: disable=C0103
except: #pylint: disable=W0702
    print('File cannot be opened:', fname)
    quit()

count = 0     #pylint: disable=C0103
for line in file_handler:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
