# Composition is a concept that models and has a relationship

import os 
os.system('cls')

# Laptop has processor, battery, screen, keyboard
# Component class

class Processor:
    def __init__(self, brand, cores):
        self.brand = brand
        self.cores = cores

    def process(self):
        print(f'Processor running with {self.cores} cores of {self.brand}')

class Battery:
    def __init__(self, capacity):
        self.capacity = capacity

    def charge(self):
        print(f'Battery charging with a capacity {self.capacity}mAH')

class Screen:
    def __init__(self, size):
        self.size = size
    
    def display(self, content):
        print(f'Displaying {content} on {self.size} inched screen')
        '''Content is not an attribute of the screen. It cannot be referred through self'''

class Keyboard:
    def __init__(self, category):
        self.category = category

    def typed_key(self, key):
        print(f'{key} is pressed on {self.category} keyboard')
        '''Key is not an attribute of the class Keyboard
           It cannot be referred through self'''
        
# Composite class
class Laptop:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        '''Create component objects'''
        self.processor = Processor('Intel I7', 8)
        self.battery = Battery(6000)
        self.screen = Screen(17)
        self.keyboard = Keyboard('Backlit')
    
    def turn_on(self):
        print(f'{self.model} of {self.brand} is turned on!!!')
        self.processor.process()
        '''Laptop object's processor component is calling process method'''

    def show_content(self, message):
        self.screen.display(message)
        '''Laptop object's screen component is calling display method to
           display the message'''
        
    def charge_laptop(self):
        self.battery.charge()
        '''Laptop object's battery component has to be charged'''

    def use_keyboard(self, key):
        self.keyboard.typed_key(key)
        '''Laptop object's keyboard component will know what
           key has been pressed'''
        
# Composite Object Creation

l1 = Laptop('Dell', 'Inspiron 15')
l1.turn_on()

l1.show_content('Welcome, Enjoy the new laptop')

l1.use_keyboard('Tab')

l1.charge_laptop()

