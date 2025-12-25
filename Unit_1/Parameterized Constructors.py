class Addition:
    def __init__(self, f, s):
        self.f = f
        self.s = s
    
    def calculator(self):
        self.ans = self.f + self.s

    def display(self):
        print(f'The addition of {self.f} and {self.s} results in {self.ans}')

# a = Addition(10, 20)
# a.calculator()
# a.display()

# ----------------------------------------------------------------------------

class A:
    def init(self):
        print('The object has been created.')
    
# A().init()
# print(a)
# del a
# print(a)

# Destructor
class A:
    def __init__(self):
        print('The object is initialized')

    def __del__(self):
        print('The object is destroyed')

a = A()
# del a
# print(a)
# a = A().__init__()
print(a.__del__()) # It works as a normal call to a method and not as a call to the destructor
print(a) # the object is still alive since the destructor was not called
del a # This calls the destructor and destroys the object