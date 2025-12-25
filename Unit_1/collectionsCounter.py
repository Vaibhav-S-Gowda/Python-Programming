from collections import Counter
from collections import deque
#counter - counts the occurrences in an iterable or sequence

l = [1,2,3,4,1,2,4]
print(Counter(l)) # Counter({1: 2, 2: 2, 4: 2, 3: 1})

s = 'This is a statement'
print(Counter(s)) # Counter({'s': 3, ' ': 3, 't': 3, 'i': 2, 'a': 2, 'e': 2, 'T': 1, 'h': 1, 'm': 1, 'n': 1})

#Deque
d = deque([10,20,30,40,50])
type(d)

#Instertion in rear

d.append(60)
print(d) # deque([10, 20, 30, 40, 50, 60])

#Insert at front
d.appendleft(70)

#Deletion at rear
d.pop()
print(d) # deque([70, 10, 20, 30, 40, 50])

#Deletion at front
d.popleft()
print(d) # deque([10, 20, 30, 40, 50])