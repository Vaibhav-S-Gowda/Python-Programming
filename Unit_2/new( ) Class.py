import os
os.system('cls')


class NewClass1:
    def __new__(cls, a):
        # a is the placeholder for 'b' that is used for initiaizing the object.
        # The number of attributes that is used to correspond to the number of attributes in init.
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