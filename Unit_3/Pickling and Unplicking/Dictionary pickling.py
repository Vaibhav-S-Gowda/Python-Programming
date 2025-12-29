import pickle as p

d_1 = {'name':'Alpha', 'age':20, 'city':'Bangalore', 'phone': 9876543210}
with open("dict.pkl", 'wb') as f:
    p.dump(d_1, f)
with open("dict.pkl", 'rb') as f:
    p_d_1 = p.load(f)
print(f'Unpickled dictionary is {p_d_1}')

