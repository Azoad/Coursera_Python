# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
res = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    spos = line.find(' ')
    num = line[spos:]
    res = res + float(num)
    count = count + 1
print('Average spam confidence:', (res/count))