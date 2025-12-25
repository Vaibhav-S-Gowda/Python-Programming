from collections import namedtuple

Person = namedtuple('Person',{'name','age'})

p1 = Person(name = 'Alias', age = 10)
p2 = Person('Bob', 70)
p3 = Person(age = 11, name = 'Harry')

print(p1)
print(p3.name)