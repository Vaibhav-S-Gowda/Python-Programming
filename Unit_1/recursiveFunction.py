import os
os.system('cls')

# def sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sum(n - 1)

# n = int(input("Enter the number: "))
# if n < 0:
#     print(f"Sum of {n} values is not possible")
# else:
#     print(f'Sum of n is {sum(n)}')

# Recursion can cause stack overflow issues.
# Python has a built-in recurssion limit.


# ---------- Greatest Common Devisor ----------

# def gcdnm(a ,b):
#     if b == 0:
#         return a
#     return gcdnm(b, a%b)
# a = int(input("Enter the first value"))
# b = int(input("Enter the second value"))

# print(f'The GCD of {a}, {b} is {gcdnm(a,b)}')

# ----------- Factorial ----------

def factorial(n):
    if ((n == 0) or (n == 1)):
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter the number"))
print(f'The factorial of {n} is:', factorial(n))

