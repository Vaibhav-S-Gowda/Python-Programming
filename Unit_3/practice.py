# Logical errors

# def fact_cal(n):
#     r = 1
#     for i in range(n):
#         r = r*i
#     print(r)

# fact_cal(3)

# Corrected code
def fact_cal(n):
    r = 1
    for i in range(1, n+1):
        r = r*i
    print(r)
fact_cal(3)

# Runtime Errors or Exceptions
'''List of exceptions handled in Python'''

import builtins
l = [name for name in dir(builtins)
     if isinstance(getattr(builtins, name), type)
     and
     issubclass(getattr(builtins, name), BaseException)]
print('List of exceptions in Python\n')
for i in l:
    print(i, end = "    ")