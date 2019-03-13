"""some python objects"""

x = 'abc'
print(x, '->', type(x))
print('2.5 ->', type(2.5))
print('2 ->', type(2))
print('\nmethods of', type(x), '->', dir(x))

y = list()
print(y, '->', type(y))
print('\nmethods of', type(y), '->', dir(y))

z = dict()
print(z, '->', type(z))
print('\nmethods of', type(z), '->', dir(z))
