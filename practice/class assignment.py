from functools import reduce

# ub , lb = int(input("Enter upperbound: ")), int(input("Enter Lowerbound: "))

# l = list(range(lb, ub + 1))
# c = 0
# for  i in l:
#     x = i * i
#     c += x
# print(c)

print(reduce(lambda x, y: x + y, map(lambda x: x*x, range(int(input("Enter lower bound: ")), int(input("Enter upper bound: ")) + 1))))