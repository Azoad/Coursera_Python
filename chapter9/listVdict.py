"""comparison between list and dictionaries"""

lst = list()

lst.append(21)
lst.append(183)

print(lst) #list has a fixed order

lst[0] = 23

print(lst)

dct = dict()

dct['age'] = 21
dct['course'] = 183

print(dct) #dictionary's order is not fixed

dct['age'] = dct['age']+2

print(dct)


################

list = [1,'age',23,'ok']
print(list)
print(type(list))

dict = {1:'Oh!', 'age':543, 23:66, 'ok':'ok?'} #problem putting 0 at first
print(dict)
print(type(dict))