class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def barks(self):
        print(f'{self.name} says Woof')

    def sleep(self):
        print(f'{self.name} is sleeping now Zzz')

d1 = Dog('Tommy', 'German Shepherd',12)
d1.barks()
d1.sleep()

# import sys
# x = 5
# print(sys.getsizeof(x))
# y = 10**1000
# print(sys.getsizeof(y))
