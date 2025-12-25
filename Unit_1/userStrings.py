from collections import UserString

#---- Create Custom String of the type UserString
class MyString(UserString):
    def uppercon(self):
        return self.upper()
    def add_exclamation(self):
        return self.data + '!!!'
    
#--- Create an instance of Custom String
cs = MyString("Hello, how are you")
print(cs)

#--- Custom Methods
print(cs.uppercon())
print(id(cs))

cs = cs.add_exclamation()
print(cs)