import pickle as p

def greet(name):
    return f'Hello {name}'

with open('func.pkl', 'wb') as f:
    p.dump(greet, f)

with open('func.pkl', 'rb') as f:
    p_f = p.load(f)

print(p_f('Alpha'), p_f('Beta'))

