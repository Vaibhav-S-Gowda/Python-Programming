import pickle as p

# Numeric DataType

a, b, c = 10, 10.5, 10-9j

with open('numeric.pkl', 'wb') as f:
    ''' Use wb since the data has to be writte in bytestream'''
    p.dump(a, f)
    p.dump(b, f)
    p.dump(c, f)

with open('numeric.pkl', 'rb') as f:
    data = p.load(f)
    print(f'Unpickled data is {data}')

