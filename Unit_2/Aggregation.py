import os
os.system('cls')

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    def teach(self):
        print(f'{self.name} teaches {self.subject}')

class school:
    def __init__(self, name):
        self.name = name
        self.teachers = [] # List that will contain the teacher objects
    def add_teacher(self, t): 
        '''t is the object of the teacher class'''
        self.teachers.append(t)
    def show_teachers(self):
        print(f'Teachers in {self.name}: ')
        for t in self.teachers:
            print(f'{t.name} for {t.subject}')

# Create School Object
s1 = school('ABC School')
s2 = school('PQR high School')

# Create Teacher Object
t1 = Teacher('Mr. Xyz', 'Mathematics')
t2 = Teacher('Ms. Abc', 'Chemistry')
t3 = Teacher('Ms. Lmn', 'Computer Science')

# Aggregate the teachers to the school
s1.add_teacher(t1)
s1.add_teacher(t3)
s1.add_teacher(t2)

s2.add_teacher(t2)
s2.add_teacher(t3)
s2.add_teacher(t1)

s1.show_teachers()
s2.show_teachers()
