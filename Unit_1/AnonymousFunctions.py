from os import system
system("cls")

# ---------- Anonymous Functions or Lambda Functions ----------

x = lambda a: a*a
print(type(x) ,id(x)) # <class 'function'> 2452628238192

print(x(50)) # 2500

l = [1,4,5,6,78,98,98.0]
print(x(l[4])) # 6084

# Map()
b = list(map(x,l)) 
c = list(map(lambda a: a*a, l)) 
print(c) # [1, 16, 25, 36, 6084, 9604, 9604.0]
print(b) # [1, 16, 25, 36, 6084, 9604, 9604.0]

d = list(map(len, ['apple','banana','cherry','durian','enterprise','fig']))
print(d) # [5, 6, 6, 6, 10, 3]

def square(x):
    return x*x
sq = list(map(square, [1,2,3,4,5,6,7,8,9,10]))
print(sq) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

s_upper = list(map(str.upper, ['albus','peach','mercury','sisya']))
print(s_upper) # ['ALBUS', 'PEACH', 'MERCURY', 'SISYA']

# ---------- Lambda Functions 
# Condition based

is_even = lambda x: x%2 == 0
print(is_even(10)) # True
print(is_even(11)) # False

