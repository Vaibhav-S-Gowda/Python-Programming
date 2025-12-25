import os
os.system('cls')

#----------- Packing and Unpacking Variables ---------- 

(a,b,c) = [1,2,3.5]
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')
print(type(a), type(b), type(c))

(a,b,c) = ('alpha', 20, 6+7j)
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')

def unpack(values):
    a,b,c = values
    print(f'a = {a}, b = {b}, c = {c}')

unpack((23,34,45))