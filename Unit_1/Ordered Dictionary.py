from collections import OrderedDict as od
from collections import defaultdict as dd 

# Create
o_d = od({1:'a' ,2:'b' ,3:'c' ,4:'d'})
print(type(o_d))

o_d1 = od([(1,'a'), (2,'b'), (3,'c')])
print(type(o_d1))

# Move values
o_d.move_to_end(1)
print(o_d)

# Display it in reverse order
for k in o_d:
    print(k)

for k in reversed(o_d):
    print(k)

# Default Dictionary
d = { 1:'a', 2:'b'}
print(type(d))
print(d[1],d[2],d[3])

# Integer Default Dictionary
id = dd(int)
id['a'] = 1
id['b'] += 1
print(id, type(id), id['c'])

# Float default Dictionary 
id = dd(float)
id['a'] = 1
id['b'] += 1
print(id, type(id), id['c'])

# Complex default Dictionary 
id = dd(complex)
id['a'] = 1
id['b'] += 1
print(id, type(id), id['c'])

# List default Dictionary 
id = dd(list)
id['a'] = 1
id['b'] = 1
print(id, type(id), id['c'])

# Dict default Dictionary 
id = dd(dict)
id['a'] = 1
id['b'] = 1
print(id, type(id), id['c'])

# Set default Dictionary 
id = dd(set)
id['a'] = 1
id['b'] = 1
print(id, type(id), id['c'])

# Tuple default Dictionary 
id = dd(tuple)
id['a'] = 1
id['b'] = 1
print(id, type(id), id['c'])

# String default Dictionary 
id = dd(str)
id['a'] = 1
id['b'] = 1
print(id, type(id), id['c'])

# Function Default Dictionary
def valueIsNotPresent():
    return 'Value is not present'
id = dd(valueIsNotPresent)
id['a'] = 1
id['b'] = 1
print(id, type(id), id['c'])

students = [{'name':'Shanmukh', 'score':0},
            {'name':'Hemanth', 'score':23},
            {'name':'Sridhara', 'score':67},
            {'name':'Sumadhva', 'score':23}]

group_by_score = dd(list)
for s in students:
    group_by_score[s["score"]].append(s)
for score, s_list in group_by_score.items():
    print(f'Score - {score}')
    for s in s_list:
        print(f'\t--{s["name"]}')




