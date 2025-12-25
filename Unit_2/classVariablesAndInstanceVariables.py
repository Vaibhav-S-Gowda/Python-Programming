import os
os.system('cls')

class Student:
    school_name = "PES University"
    '''school name is a class variable'''
    def __init__(self, name, age):
        '''name and age are instance variable'''
        self.name = name
        self.age = age

    def show(self):
        print(f'The student {self.name} of {self.age} years is studying in {self.school_name}')
        print(f'The student {self.name} of {self.age} years is studying in {Student.school_name}')

s1 = Student('ABC', 20)
s2 = Student('PQR', 18)
s3 = Student('ABC', 20)
s4 = Student('XYZ', 19)

s1.show()

print(Student.school_name)
print(s4.school_name)

# Modify Class Variable

s1.school_name = 'PESU'
'''A new copy of school_name is created for the s1'''
'''In this copy the value is changed to PESU'''
'''The class variable still has the old value'''
s1.show()

s2.show()

Student.school_name = 'PESU'
'''The original memory location of school_name gets the new value
   PESU and is now reflected for all objects that have not created
   their own instance-level copy of school_name'''

s1.show()
s2.show()

# Modify Instance Variables


# Dynamically adding class variables

Student.address = 'RR Campus'
'''This applies for the previously created objects of the same class
   No need to recreate the old objects'''

print(s1.school_name, s1.address)

print(s2.school_name, s2.address)
print(s3.school_name, s3.address)
print(s4.school_name, s4.address)

# Dynamically Adding Instance Variables
s1.fname = 'PQR'
s3.fname = 'XYZ'
'''fname is added as an attribute to only s1, s3 it does not
   get reflected in s2, s4'''

print(s1.name, s1.age, s1.fname)
# print(s2.name, s2.age, s2.fname) #AttributeError: 'Student' object has no attribute 'fname'
print(s3.name, s3.age, s3.fname)