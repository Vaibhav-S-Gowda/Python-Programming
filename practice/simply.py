# var=10
# for i in range(10):
#     for j in range(2,10,1):
#         if var % 2 == 0:
#             continue   
#         var+=1
# else:
#     var+=1
# print(var)

# for num in range(10,14):
#     for i in range(2,num):
#         if num%i==1:
#             print(num)
#             break

# print(list(range(-1,-10,-1)))

# word = "listen"
# candidates = ["silent", "hello", "enlist", "google", "tinsel"]

# anagrams = [w for w in candidates if sorted(w)==sorted(word)]
# print(anagrams)

# class Animals:
#     def __init__(self):
#         print('The class called Animals is CREATED.')
    
#     def __del__(self):
#         print('The destructor is called for deleting the Animals.')

# obj = Animals()
# help(obj.__init__)
# # del obj

# A = set({4,8})
# B = frozenset([1, 2, 3])

# A.add(B)
# print(A)

def double(x):
    return x * 2

nums = [1, 2, 3, 4]

mapped = map(double, nums)

print(mapped)          # map object
print(list(mapped))    # [2, 4, 6, 8]
