from collections import UserList

# Create a custom list of the type UserList
class CustomList(UserList):
    def addTwice(self, value):
        self.data.append(value)
        self.data.append(value)
    def remtwice(self, pos):
        self.data.pop(pos)
        self.data.pop(pos)

# Create an instance of CustomList
cl = CustomList([1,2,3,4,5,6,7])
cl.append(8)
print(cl) # [1, 2, 3, 4, 5, 6, 7, 8]

cl.extend([9,10])
print(cl) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cl.insert(0,0)
print(cl) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cl.pop(3)
print(cl) # [0, 1, 2, 4, 5, 6, 7, 8, 9, 10]

cl.remove(4)
print(cl) # [0, 1, 2, 5, 6, 7, 8, 9, 10]

cl.reverse()
print(cl) # [10, 9, 8, 7, 6, 5, 2, 1, 0]

cl.sort()
print(cl) # [0, 1, 2, 5, 6, 7, 8, 9, 10]

#-------- Custom Methods
cl.addTwice(12)
print(cl) # [0, 1, 2, 5, 6, 7, 8, 9, 10, 12, 12]

cl.remtwice(5)
print(cl) # [0, 1, 2, 5, 6, 9, 10, 12, 12]