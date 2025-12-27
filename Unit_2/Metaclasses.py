import os
os.system('cls')

# Creation of a class using type
def greet(self):
    print(f'Hello {self.name}')

# Create the class and attach the method to the class
Student = type('Student', (object,), {'greet':greet, 'name':'XYZ'})
'''type takes in three parameters
   name - name of the class
   base - tuple that consists of the base classes
   dictionary - a key vvalue pair of every method and attribute'''

# Create the object of the class
s = Student()
print(type(s))

# Creation of Custom Metaclass
class RequiredID(type):
    '''To create a metaclass it has to inherit from type
       type builds classes'''
    def __new__(cls, name, bases, attr):
        '''custom new method is defined
           parameters are
           cls - metaclass itself
           name - name of the class being created
           bases - tuple of base class
           attr - dictionary of attributes and method of the class'''
        if 'id' not in attr:
            attr['id'] = 100
        '''Check whether an attribute called as id exists
           if the class does not define id a default attribute if is added with a value of 100'''
        return super().__new__(cls, name, bases, attr)
        '''Calling types's new method'''

# Create a class that uses custom meta class

class Student(metaclass = RequiredID):
    '''metaclass = Required tells Python to use
       RequiredID as the metaclass and not the default metaclass
       name - Student
       bases - empty tuple since it does not inherit any other
       class except the metaclass
       attr - should be the dictionary of attributes and methods.
       In this example keep it empty'''
    def __init__(self, name):
        self.name = name

s = Student('ABC')
print(s.name)
print(s.id)

class Teacher(metaclass = RequiredID):
    id = 20
    def __init__(self, name):
        self.name = name

t = Teacher('BAA')
print(t.name)
print(t.id)


