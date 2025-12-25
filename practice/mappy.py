lst = [1,2,3,4,5,6,7,8,9,0]

def fun(x):
    return x**2

sq_lst = list(map(fun, lst))
print(sq_lst)

# ---------- Lambda Function ----------

sq_lst = list(map(lambda x: x**2, lst))
print(sq_lst)
