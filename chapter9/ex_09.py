"""Worked exercise"""

fname = input('Enter file: ')
if len(fname) < 1:
    fname = 'E:/Coursera/py4e/files/clown.txt'
fhand = open(fname)

dictionary = dict()
for line in fhand:
    line = line.rstrip()
    print('Plain text:', line)

    words = line.split()
    print('\nList of words:', words)

    print('\nWord and count:')
    for word in words:
        # print(word)
        print('***', dictionary.get(word, -99))
        if word in dictionary:
            dictionary[word] = dictionary[word] + 1
            # print('***Existing***')
        else:
            dictionary[word] = 1
            # print('***NEW***')
        # print(dictionary[word])
        print(word, dictionary[word])

print('\nDictionary:', dictionary)
