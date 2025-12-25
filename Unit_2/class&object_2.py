class Laptop:
    # ___init__() method gets called automatically when the object has been created for this class.
    # This function initiaizes the value associated with the object.
    # self - represents the object and should be the first parameter
    def __init__(self ,brand, model, price = 45000):
        self.brand = brand # associating the current object's brand value
        self.model = model
        self.price = price
        self.battery_level = 100 # initial battery level

    def turn_on(self):
        '''self represents the current object that has called this method'''
        print(f'{self.model} of {self.brand} is now ON')
    
    def specifications(self):
        print(f'LAPTOP DETAILS\nBrand: {self.brand}\nModel: {self.model}\nPrice: Rs.{self.price}')

    def turn_off(self):
        print(f'{self.model} of {self.brand} is now OFF')
    
    def check_battery(self):
        print(f'This laptop has {self.battery_level}% battery remaining')

    def update_battery_status(self, val):
        if 0 <= val <= 100:
            self.battery_level = val
            print(f'Battery level of {self.model}, {self.brand} is updated to {self.battery_level}')
        else:
            print('Invalid battery level!!! Please enter a value between 0 - 100')

    def decrease_battery(self, usage):
        if usage < 0:
            print('Usage amount cannot be negative')
        elif self.battery_level - usage <= 0:
            print('Battery level too low! Please charge the Laptop')
            self.battery_level = 0
        else:
            self.battery_level = self.battery_level - usage
            print(f'Battery decreased by {usage}%. Current level: {self.battery_level}')

l1 = Laptop('Dell','Inspiron 15',60000)
print(l1.brand,l1.model,l1.price,l1.battery_level)

l1.check_battery()

# ---------- Modification of attribute values once the object has been created ----------
# Change the value directly using the object
l1.battery_level = 90
l1.check_battery()

# Use a method that sets a new value each time the method is called
l1.check_battery()
l1.turn_on()
l1.update_battery_status(85)
l1.check_battery()
l1.turn_off()

# Increment or Decrement an attribute using a method
l1.turn_on()
l1.decrease_battery(20)
l1.check_battery()