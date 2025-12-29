import pickle as p

# Multiple Objects
l1 = [1, 2, 3, 'apple', [2, 3, 4], 89+9j]
d1 = {1:2, 3:4}
s1 = 'Hello Pickling'
with open('all.pkl', 'wb') as f:
    p.dump(l1, f)
    p.dump(d1, f)
    p.dump(s1, f)
with open('all.pkl', 'rb') as f:
    p_l1 = p.load(f)
    p_d1 = p.load(f)
    p_s1 = p.load(f)
print(p_l1)
print(p_d1)
print(p_s1)

