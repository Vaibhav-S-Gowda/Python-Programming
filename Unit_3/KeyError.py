# d = {'name' : 'Alpha', 'age':20, 'city':'Bengaluru'}
# print(d['address']) # KeyError: 'address'


# LookupError
try:
    d = {'name' : 'Alpha', 'age':20, 'city':'Bengaluru'}
    d['address']
except LookupError as e:
    print(f'LookupError: {e}')
