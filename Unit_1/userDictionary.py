from collections import UserDict

# Creation of user Dictionary

class MyUserDict(UserDict):
    def get_keys(self):
        return {keys.upper() for keys in self.keys()}
    
# Create an instance of my userDict
cd = MyUserDict({'apple':10, 'banana':20, 'cherry':30})
print(cd)
print(type(cd))
print(cd.get_keys())
cd.keys()

