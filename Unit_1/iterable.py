l = [1,2,3,4,5]
l_iter = iter(l)
print(type(l),type(l_iter))
print(next(l_iter), end = " ")
print(l_iter.__next__(), end = " ")
print(l_iter.__next__(), end = " ")
print(l_iter.__next__(), end = " ")
print(l_iter.__next__())
# print(l_iter.__next__()) # ERROR: StopIteration

# n = 123456789
# n_iter = iter(n) # TypeError: 'int' object is not iterable

str = 'Python Programming'
s_iter = iter(str)
print(type(str), type(s_iter))

t = (1,2,3,4,5)
t_iter = iter(t)

d = {1:2, 3:4, 5:6, 7:8, 9:8}
d_iter = iter(d)
print(d_iter, ) # <dict_keyiterator object at 0x000001B0D45FC4A0>
print(d_iter) # <dict_keyiterator object at 0x000001B0D45FC4A0>
print(type(d), type(d_iter))

# -------------------- Infinite Cycle --------------------

import itertools as it
seq = it.chain(['A','B','C','D','E','F','G','H'])
seq_iter = iter(seq)
for _ in range(5):
    print(next(seq_iter), end =" ")

for _ in range(3):
    print(next(seq))

# -------------------- Stop Iteration -------------------- 

s = {1,2,3,4,5}
s_iter = iter(s)
try:
    while True:
        print(next(s_iter))
except StopIteration:
    print("Completed")