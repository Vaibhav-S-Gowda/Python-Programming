def fact_cal(n):
    for i in range(1, n+1):
        r = r*i # UnboundLocalError: local variable 'r' referenced before assignment
    return r

print(fact_cal(5))