from os import system
system('cls')

class sample:

    a = 10
    b = 20

print(sample.a)
print(sample.b)

sample.a = 100
sample.b = 200
print(sample.a)
print(sample.b)

s = sample()
print(s.a)
print(s.b)

s.a = 1000
s.b = 2000
print(s.a)
print(s.b)

print(sample.a)
print(sample.b)

print(s.__dict__)
print(sample.__dict__)