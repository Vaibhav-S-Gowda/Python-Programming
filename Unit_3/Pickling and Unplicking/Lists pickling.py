import pickle as p

l1= ['apple', 23, 56, 78, 'BANANA', 89-9j, ['a', 'b','c']]
with open('list.pkl', 'wb') as f:
    p.dump(l1, f)

with open('list.pkl', 'rb') as f:
    p_l1 = p.load(f)
print(f'Unpickled list is {p_l1}')
print(f'Type of p_l1 is {type(p_l1)}')
print(f'Type of "f" is {type(f)} and type of "list.pkl" is {type("list.pkl")}')

