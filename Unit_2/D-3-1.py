class Student:
    university_name = "PES University"
    
    def __init__(self, name, marks):
        self.name = name
        
        if not Student.is_valid_mark(marks):
            print(f'Warning: Invalid mark {marks} provided for {name}. Setting marks to zero')
            self.marks = 0
        else:
            self.marks = marks
            
    # Class Method: Operates on the class and its class variables
    @classmethod
    def update_university_name(cls, new_name):
        print(f'\n--- Class Method: Updating University Name ---')
        print(f'Old Name: "{cls.university_name}" -> New name: "{new_name}"')
        cls.university_name = new_name
        
    @staticmethod
    def is_valid_mark(mark) -> bool:
        return 0 <= mark <= 100
        
    def print_details(self):
        mark_status = "Valid" if Student.is_valid_mark(self.marks) else "Invalid"
        print(f"Name: {self.name:<15} | Marks: {self.marks:<4} ({mark_status}) | University: {self.university_name}")

print("--- Initial Student Creation ---")

student_a = Student("Alice", 85)
student_b = Student("Shanmukha", 92)
student_c = Student("Mulla", 110)

print('\n--- Phase 1: Details with Initial University Name ---')
student_a.print_details()
student_b.print_details()
student_c.print_details()

Student.update_university_name("Global Institute of Research")

print('\n--- Phase 2: Details with Updated University Name ---')
student_a.print_details()
student_b.print_details()
student_c.print_details()