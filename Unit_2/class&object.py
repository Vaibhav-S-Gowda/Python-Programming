class Laptop:
    # ___init__() method gets called automatically when the object has been created for this class.
    # This function initiaizes the value associated with the object.
    # self - represents the object and should be the first parameter
    def __init__(self ,brand, model, price = 45000):
        self.brand = brand # associating the current object's brand value
        self.model = model
        self.price = price

    def turn_on(self):
        '''self represents the current object that has called this method'''
        print(f'{self.model} of {self.brand} is now ON')
    
    def specifications(self):
        print(f'LAPTOP DETAILS\nBrand: {self.brand}\nModel: {self.model}\nPrice: Rs.{self.price}')

    def turn_off(self):
        print(f'{self.model} of {self.brand} is now OFF')

print(type(Laptop), id(Laptop))

# ---------------------- Object Creation ---------------------- 
l1 = Laptop('Dell', 'Inspiron 15', 60000)
l2 = Laptop('ASUS', 'TUF - F15', 93000)
print(type(l1), id(l1),'\n',type(l2), id(l2))

l3 = Laptop(25000, 'HP','Pavillion')
print(id(l3))

l4 = Laptop(price = 250000, model = 'M4' ,brand='Apple')
print(id(l4),type(l4))

l5 = Laptop('Accer','X')

# Accessing the data members in an object
print(f'I own a {l1.model} of {l1.brand} that costs Rs.{l1.price}')
print(f'I own a {l2.model} of {l2.brand} that costs Rs.{l2.price}')
print(f'I own a {l5.model} of {l5.brand} that costs Rs.{l5.price}')

# Accessing Mothods through objects
l1.turn_on()
l2.specifications()

l8 = ('Dell','Inspiron 17',67000)
l8.turn_on()
# L8 is the positional argument that is recieved as self in the method
# Every method defined in a class should take self as a parameter if the object needs to call the method
