# Scenario: Class Car having the attribute of model and year and has the methods of drive, stop, read the odometer and update. 
# Create an electric car that the attribute battery and has the method read battery/check battery and also displays how much time before a recharge.

# Parent Class
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.odometer = 0
        self.is_running = False

    def drive(self):
        if not self.is_running:
            self.is_running = True
            print(f'{self.model} of year {self.year} is now in drive mode')
        else:
            print(f'{self.model} is already driving')

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f'{self.model} of year {self.year} is stopped')
        else:
            print(f'{self.model} is already stopped')

    def update_odometer(self):
        print(f"The car's odometer displays {self.odometer}")

    def inc_odometer(self, accelrate):
        if not self.is_running:
            print(f'Cannot increase speed — {self.model} is stopped!')
            return

        if accelrate < 0:
            print('Acceleration cannot be negative')
        else: 
            self.odometer += accelrate
            print(f'Car speed increased by {accelrate} km/h. Current speed: {self.odometer} km/h')

# Child Class
class Electric(Car):
    def __init__(self, model, year, battery, time):
        super().__init__(model, year)
        self.battery = battery      # battery capacity in percentage
        self.time = time            # estimated time before recharge in hours
    def read_battery(self):
        print(f"The current battery level is {self.battery}%")

    def check_battery(self):
        if self.battery > 80:
            print("Battery level is high. You can drive comfortably.")
        elif 40 <= self.battery <= 80:
            print("Battery level is moderate. Consider charging soon.")
        else:
            print("Low battery! Please recharge immediately.")

    def recharge_time(self):
        print(f"Approximately {self.time} hours left before the next recharge is needed.")


# Example Usage
my_ev = Electric("Tesla Model 3", 2024, battery=75, time=3)

my_ev.drive()
my_ev.read_battery()
my_ev.check_battery()
my_ev.recharge_time()
my_ev.inc_odometer(50)
my_ev.read_battery()
my_ev.stop()
my_ev.update_odometer()
my_ev.inc_odometer(50)