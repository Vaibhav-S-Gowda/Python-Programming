import os
os.system('cls')

#--------------- Scope of the variable in functions

# def outer():
#     x = 10
#     print(f'Memory location of x is: {id(x)}')
#     print(f'x in outer = {x}')
#     def inner():
#         y = 10 + 5j
#         print(f'Memory location of y in inner is: {id(y)}')
#         print(f'y in inner = {y}')
#     inner()
#     print(f'Memory location of x is: {id(x)}')
#     print(f'x in outer = {x}')
# outer()

#---------------- Passing Arguments to Nested Functions

def outer(n):
    print(f'The value of n in outer is {n}')
    def inner():
        m = int(input("Enter the value"))
        print(f'The value of n in inner is {m}')
        print(f'The value of n in inner is {n}')
    inner()
    print(f'The value of n in outer is {n}')
n = input("Enter the value")
(int)(n)
outer(n)