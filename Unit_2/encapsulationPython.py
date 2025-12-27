# class Employee:
#     def __init__(self, name, dept, salary):
#         self.name = name
#         self.dept = dept
#         self.salary = salary

#     def show(self):
#         print(f'I am {self.name} working in {self.dept} for Rs.{self.salary}')

# e1 = Employee('ABC', 'PQR', 150000)
# e2 = Employee('XYZ', 'PQR', 130000)

# e1.show() # Encapculation at class level
# e2.show() # Encapculation at class level



# Access specifiers
class Employee:
    def __init__(self, name, dept, salary):
        self.name = name #public access
        self._dept = dept #protected access
        self.__salary = salary # private access
    # Public Method to access the data members
    def show(self):
        print(f'I am {self.name} woking in {self._dept} for Rs. {self.__salary}')

    # Protected Method to access the data members
    def _display(self):
        print(f'I am {self.name} woking in {self._dept} for Rs. {self.__salary}')

    # Private Method to access the data members
    def __see(self):
        print(f'I am {self.name} woking in {self._dept} for Rs. {self.__salary}')

e1 = Employee('ABC', 'HR', 150000)
# --- Accessing data members from outside the class
# Use the object and the data member
print(e1.name)
print(e1._dept)
# print(e1.__salary) # This line of code throws an error

# Use public method to access the data from outside of the class
e1.show()

# Use Name Mangling
print(e1._Employee__salary)