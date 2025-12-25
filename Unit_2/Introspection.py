import os
os.system('cls')

l = [1,2,3,4]
s = 'Hello'
t = (1,2,3)
sets = {1,2,3}
d = {1:2, 2:3, 3:4}
n = 123

# print(dir(l))
# print(l.__add__([5]))
# print(l.__class__)
# print(l.__sizeof__())
# print(l.__hash__)
# print(l.__contains__(10))

# print(dir(s))
# print(s.endswith('o'))

# print(t.__add__((23,)))
# print(id(t))
# print(dir(t))

# print(dir(sets))
# print(dir(d))

# print(dir(n))

print(type({}), type(()), type([]))

# -------------------------

import os
def f():
    pass
print(type(os), type(f))

# id()
print(id(os), id(1), id(True), id([]), id({}), id(''), id(""),id(''''''), id(()))

# hasattr()
class A:
    def __init__(self, b, m):
        self.b = b
        self.m = m
    def show(self):
        print(f'{s.b} having {s.m}')
obj = A('X', 'x')
print(hasattr(obj, 'show'))

