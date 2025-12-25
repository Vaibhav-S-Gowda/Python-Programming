# li=['a','b','c','d','e','f','g','h']
# print(li[10:])

# list = [6,'b','c'] * 2; print(list)

l1=[]
l1.append([1,[2,3],4])
print(l1)      
l1.extend([7,8,9,[10,11]])
print(l1)      
print(l1[0][1][1]+l1[2])

l1.insert(2,[8.7])
print(l1)