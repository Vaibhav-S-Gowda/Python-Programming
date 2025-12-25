#  --- Function Definition
def add(a, b):
    return a+b

# ---- Calling a function
print(add(10, 20)) # 30
c = add(2, -3)
print(c) # -1

print(add(34.0, 32)) # 66.0
print(add(32+34j, 32+56j)) # (64+90j)
print(add(32.34, 32+56j)) # (64.34+56j)
print(add('apple', 'banana')) # applebanana
print(add([1,2,3], ['banana'])) # [1, 2, 3, 'banana']

#------Keyword Arguments
print(add(b = 89, a = 60))

# ---- Default Arguments
def add(a = 10, b = 20):
    return a + b
print(add()) #30
print(add(-10)) #10
print(add(b = -10)) #0

#---- Variable Length Arguments
def add(*n):
    sum = 0
    for i in n:
        sum += i
    return sum

print(add(10, 20, 30, 40, 50, 60))

#---- Variable with required/keyword/default
def add(*n, a, b):
    sum = 0
    for i in n:
        sum += i
    sum += a
    sum += b
    return sum

# print(add(10, 20, 30)) # TypeError: add() missing 2 required keyword-only arguments: 'a' and 'b'
print(add(a = 20, b = 30)) #50


#----- Variable with default
def add(*n, a = 10, b = 40):
    sum = 0
    for i in n:
        sum += i
    sum += a
    sum += b
    return sum

print(add(10)) #60
print(add(10, 20, 30)) #110

#------ Pass By Reference

l = [1, 2, 3, 4]
print(id(l))

def list_mod(l):
    l.append(20)
    l.append(30)
    print(l) #[1, 2, 3, 4, 20, 30]
    return

list_mod(l)
print(l, id(l))

def con(a, b):
    a += b
    return a
a = 'Hello'
b = 'World'
con(a, b)
print(id(a), id(b))