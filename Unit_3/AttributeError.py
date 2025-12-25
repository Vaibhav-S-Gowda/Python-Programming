# s = "Hello to Errors"
# s.reverse()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f'Hello, My name is {self.name})')

p = Person('Ironman', 40)
p.city # AttributeError: 'Person' object has no attribute 'city'