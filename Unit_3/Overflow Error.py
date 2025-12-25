import math
# math.exp(1000) # OverflowError: math range error
# pow(3.14,1000) # OverflowError: (34, 'Result too large')

def fact_cal(n):
    r = 1
    for i in range(1, n+1):
        r*=i
    return r
# print(fact_cal(1000))

# print(fact_cal(40000))

# ZeroDivisionError
print(10.0/0)
print(10/0)