"""Worked exercise"""

fname = input('Enter file: ')
if len(fname) < 1:
    fname = 'E:/Coursera/py4e/files/clown.txt'
fhand = open(fname)

# print(fhand.read())

print('Plain text:')
dictionary = dict()
for line in fhand:
    line = line.rstrip()
    print(line)

    words = line.split()
    print('\nList of words:', words)

    print('\nWord and count:')
    for word in words:
        # print(word)

        """# method 1
        print('***', word, dictionary.get(word, -99))

        # method 2
        # if the key is not there then the count is zero
        oldcount = dictionary.get(word, 0)
        print(word, 'old', oldcount)
        newcount = oldcount + 1
        dictionary[word] = newcount
        print(word, 'new', newcount)
        # these four lines in one line
        dictionary[word] = dictionary[word] + 1
        print(word, 'new', dictionary[word])"""

        # method 3
        if word in dictionary:
            dictionary[word] = dictionary[word] + 1
            print('***Existing***')
        else:
            dictionary[word] = 1
            print('***NEW***')
        # print(dictionary[word])
        print(word, dictionary[word])

print('\nDictionary:', dictionary)

# the most common word
largest = -1
theword = None
for k, v in dictionary.items():
    #print(k, v)
    if v > largest:
        largest = v
        theword = k

print(theword, largest)
