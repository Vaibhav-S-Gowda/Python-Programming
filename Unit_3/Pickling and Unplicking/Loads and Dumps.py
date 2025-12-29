import pickle as p

# Load and dumps

# dump - seralize the data into a file
# load - deserialize data from a file
# dumps - serialize the data as byte in memory
# loads - deserialize bytes into data

a = 10
p_a = p.dumps(a)
print(p_a, type(p_a))
print(p.loads(p_a), type(p_a))

b, c, d = 45.7, 9+0j, "Hello"
p_b = p.dumps(b)
p_c = p.dumps(c)
p_d = p.dumps(d)

print(f'Deserialized data is {p.loads(p_b)}, {p.loads(p_c)}, {p.loads(p_d)}')