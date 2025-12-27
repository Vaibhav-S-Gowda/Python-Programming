# A course class uses a class method to build objects with default credits. 
# You must create three courses using this method and print details.

import os
os.system('cls')

class Course:
    default_credits = 3
    
    def __init__(self, name: str, credits: int):
        '''Initializes a new Course object.'''
        self.name = name
        self.credits = credits
        
    @classmethod
    def create_with_default_credits(cls, name: str):
        print(f"-> Creating new course '{name}' using default credits: {cls.default_credits}")
        return cls(name, cls.default_credits)
        
    def print_details(self):
        print(f'Course: {self.name:<30}  | Credits: {self.credits}')
        
        
print("--- Creating Courses ---")

course1 = Course.create_with_default_credits("Introduction to Python")
course2 = Course.create_with_default_credits("Data Structures & Algorithm")
course3 = Course.create_with_default_credits("Linear Algebra")

print("\n--- Printing Course Details ---")

course1.print_details()
course2.print_details()
course3.print_details()

print('\n--- Verification ---')

course_custom = Course("Advanced Research Seminar", 6)
course_custom.print_details()