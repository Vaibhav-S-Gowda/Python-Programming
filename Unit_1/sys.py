import sys

# print('Enter the user name')
# u_name = sys.stdin.readline().rstrip('\n') #Equivalent to u_name = input("Enter the user name")

# sys.stdout.write(u_name + '\n\n') #Equivalent to print(u_name); print('\n)

# sys.stderr.write('This is error message') #Exception Handling 

#Get the size of variables
n = 1234567890
lst1 = [1,2,3,4,5,6,7,8,9,0]
lst2 = ['1','2','3','4','5','6','7','8','9','0']
set1 = {1,2,3,4,5,6,7,8,9,0}
set2 = {'1','2','3','4','5','6','7','8','9','0'}
tuple1 = (1,2,3,4,5,6,7,8,9,0)
tuple2 = ('1','2','3','4','5','6','7','8','9','0')
dict1 = {1:2, 2:3, 3:4, 4:5, 5:6, 6:7, 7:8, 8:9, 9:0}
dict2 = {'1':'2', '2':'3', '3':'4', '4':'5', '5':'6', '6':'7', '7':'8', '8':'9', '9':'0'} 
dict3 = {}
f = 12345.67890
c = 89 + 9j

print(f'The size of {n} is {sys.getsizeof(n)} bytes')
print(f'The size of {lst1} is {sys.getsizeof(lst1)} bytes')
print(f'The size of {lst2} is {sys.getsizeof(lst2)} bytes')
print(f'The size of {set1} is {sys.getsizeof(set1)} bytes')
print(f'The size of {set2} is {sys.getsizeof(set2)} bytes')
print(f'The size of {tuple1} is {sys.getsizeof(tuple1)} bytes')
print(f'The size of {tuple2} is {sys.getsizeof(tuple2)} bytes')
print(f'The size of {dict1} is {sys.getsizeof(dict1)} bytes')
print(f'The size of {dict2} is {sys.getsizeof(dict2)} bytes')
print(f'The size of {f} is {sys.getsizeof(f)} bytes')
print(f'The size of {c} is {sys.getsizeof(c)} bytes')

sys.exit(0)