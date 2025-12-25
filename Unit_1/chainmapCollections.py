from collections import ChainMap as cm

# Creation
d = { 1: 'a', 2: 'b'}
d1 = { 2: 'c', 3: 'd'}
d2 = { 4: 'e', 5: 'f'}

c = cm (d, d1, d2)
print(c)
print(type(c))

# Accessing values of a chainmap
print(c[1])
print(c[4])
print(c[5])

# Adding a new chain at the front of a chainmap
print(id(c))
c = c.new_child({ 4:'g', 6:'h', 7:'i'}) #ChainMaps are immutable but we are overiding it at the memory and hence we have to assign it to a variable
print(c)
print(id(c))

# View all maps except the first map
print(c.parents)

# Ways to display
# (variable).items() - key value
# (variable).keys() - key 
# (variable).values() - value 
