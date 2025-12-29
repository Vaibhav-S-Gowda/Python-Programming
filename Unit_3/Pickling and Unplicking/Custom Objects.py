import pickle as p

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name: {self.name}, age: {self.age})'
    
p1 = Person('Alpha', 24)

with open('obj.pkl', 'wb') as f:
    p.dump(p1, f)
with open('obj.pkl', 'rb') as f:
    p_obj = p.load(f)
print(f'Unpickled object is: {p_obj}')

