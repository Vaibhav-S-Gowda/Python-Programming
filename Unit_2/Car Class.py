#  A car has a model & year the car can be started and can be stopped. Every car has an initial reading of 0.

class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.reading = 0

    def start(self):
        print(f'The car {self.model} has begun to race')

    def stop(self):
        print(f'The car {self.model} has stopped')
        self.reading = 0
    
    def car_speed_status(self, val):
        if 0 <= val <= 100:
            self.reading = val
            print(f'Speed of {self.model}, is moving at {self.reading} kmph')
        else:
            print('Car is moving really fast please reduce the speed')

c1 = Car('BMW i7', 2025)
c1.start()
c1.car_speed_status(100)
c1.car_speed_status(110)