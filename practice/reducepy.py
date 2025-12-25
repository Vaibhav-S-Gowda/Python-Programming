from functools import reduce

lst = [10, 30, 50, 70, 90]
res = reduce(lambda x,y : x+y, lst)
print(res) # 250


def sum_of_all(x,y):
    return x+y

res = reduce(sum_of_all, lst)
print(res) # 250 