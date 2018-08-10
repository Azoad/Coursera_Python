"""read all words from a file and put all as dictionary keys"""

fname = input("Enter file name: ")
fh = open(fname)
words = list()
counts = dict()

for line in fh:
    words = words + line.split()

print(words)

for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)

string = input('Enter a world to look in the dictionary: ')

print(string, 'is in the dictionary:', string in counts)
