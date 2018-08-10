counts = dict()

letters = ['a','b','c','d','b','a','a','c']

for letter in letters:
    if letter not in counts:
        counts[letter] = 1
    else:
        counts[letter] = counts[letter]+1

print(counts)        