import os
os.system('cls')

class CMeta(type):
    def __new__(cls, n, b, d):
        print(f'Creating a class {n}')
        d['Created_by'] = 'CMeta'
        d['Created_on'] = '14 November'
        return super().__new__(cls, n, b, d)
    
# Use Metaclass Keyword
class ExampleA(metaclass = CMeta):
    def greet(self):
        print('Hello from ExampleA')

# Inheriting from a class that uses the custom metaclass
class ExampleB(ExampleA):
    def greet(self):
        print('Hello from ExampleB')

ExampleA().greet()
ExampleB().greet()

# Check for the attributes added by the custom Metaclass
print(ExampleA().Created_on)
print(ExampleA().Created_by)

class ExampleC(ExampleB):
    def greet(self):
        print('Hello from ExampleC')

print(ExampleC().Created_on)