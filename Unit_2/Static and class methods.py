# Static Methods
class NewClass:
    val = 0

    def __init__(self, value):
        self.value = value

    @staticmethod
    def count():
        NewClass.val += 1
    def show(self):
        print(f'The number of objects created is {NewClass.val}')

o = NewClass(10)
o.count()
o.show()

NewClass(20).count()
NewClass(20).show()

o.count()       

# Class Methods
class NewClass:
    val = 10
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @classmethod
    def incr(cls, x):
        cls.val += x

    def show(self):
        print(f'The attribute is {self.a}, {self.b}, the value is {NewClass.val}')

z = NewClass(10, 3)
z.incr(10)
z.show()

z1 = NewClass('Hello', 'python!!')
z1.incr(25)
z1.show()

z.show()

# New()
class NewClass1:
    def __new__(cls, a):
        print('------------- Inside new method -------------')
        i = super().__new__(cls) 
        '''super() refers to the parent class which is the built-in object class
                equivalent to object.__new__(cls)
                creates a new, empty instance of cls'''
        return i 
    def __init__(self, b):
        print('Inside init method')
        self.b = b
    def show(self):
        print(f'The stored value is {self.b}')

y = NewClass1(10)
y.show()