# Get the list of even numbers

def is_even(n):
    if n % 2 == 0:
        return n

l = list(filter(is_even, range(20)))
print(l) # [2, 4, 6, 8, 10, 12, 14, 16, 18]

l = list(filter(lambda x: x%2 == 0, range(20)))
print(l) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Reduce()
# reduce(callable,iterable)
# callable - lambda/user-defined/built-in functions
# iterable - string/list/set/tuple/dictionary
# output - 1 output

# Sum of numbers

from functools import reduce
l = reduce(lambda a,b: a + b, [1,2,3,4,5,6,7,8,9,10])
print(l) # 55

# Zip()
# zip(iterables...)

l = list(zip([1,2,3,4,5],['a','b','c','d','e'],[0.0,1.1,2.2,3.3,4.4]))
print(l) # [(1, 'a', 0.0), (2, 'b', 1.1), (3, 'c', 2.2), (4, 'd', 3.3), (5, 'e', 4.4)]

l = list(zip([1,2,3,4,5,6,7,8,9,10],['a','b','c','d','e']))
print(l) # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

# Max()
# max(values)
# values = same type (except complex)
# output - largest or lexicographically largest value

a = max('a','A','aa','AA')
print(a) # aa

print(max([1,2,3,4],[1,2,4,5],[1,2,6,7],[1,2,6])) # [1, 2, 6, 7]

# min(values)
# values - same type(except complex)
# output - smallest / lexicographically smallest

print(min('a','A','aa','AA')) # A
print(min([1,2,3,4],[1,2,3],[1,2,3,5],[1,2,6])) # [1, 2, 3]

# Operators

import operator as o
print(o.add(10, 20)) # 30
print(o.add(10, -20)) # -10

# sub(), truediv(), floordiv(), mul(), add(), mod(), gt(), ge(), le(), lt(), eq(), ne()
# or_, and_, not_, xor_

