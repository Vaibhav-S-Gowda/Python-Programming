# Parent Class
class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.battery_level = 100

    def turn_on(self):
        print(f'{self.model} of {self.brand} is now turned ON')

    def turn_off(self):
        print(f'{self.model} of {self.brand} is now turned OFF')

    def check_battery(self):
        print(f'The laptop has {self.battery_level}% battery remaining')

    def dec_battery(self, usage):
        if usage < 0:
            print('Usage amount cannot be negative')
        elif self.battery_level-usage < 0:
            print('Battery too LOW. Please charge the Laptop')
        else: 
            self.battery_level -= usage
            print(f'Battery decreased by {usage}%. Current level: {self.battery_level}')

# Child Class
class GamingLaptop(Laptop): 
    '''Inherits the attributes from the parent class Laptop'''
    def __init__(self, brand, model, price, gpu, RAM):
        '''Initialize the attributes of the parent class'''
        super().__init__(brand, model, price)
        '''This is a call and not definition'''
        '''self is taken from the child object that wants to be initialized'''
        self.gpu = gpu
        self.RAM = RAM

    # Methods of Child Class
    def boost_mode(self):
        print(f'{self.model} of {self.brand} is running in Boost Mode with {self.gpu} and {self.RAM}')

    # Method Overriding from parent class
    def turn_on(self):
        super().turn_on() # call the method of the parent class
        return f'{self.model} of {self.brand} is starting in high performance gaming mode with {self.gpu}'
    
# Object Initialization
l1 = Laptop('Asus', 'Vivobook', 100000)
gl1 = GamingLaptop('Asus', 'Rog Strix', 150000, 'NVIDIA RTX 4070', 64)

# Parent Class Usage
l1.turn_on()

l1.check_battery()
l1.dec_battery(10)

# Child Class usage
gl1.turn_on() 
gl1.boost_mode()
gl1.dec_battery(15)
gl1.check_battery()