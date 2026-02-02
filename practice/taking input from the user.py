n = int(input("How many elements in the list? "))

my_list = []
for i in range(n):
    value = input("Enter element: ")
    my_list.append(value)

print("List =", my_list)

n = int(input("How many elements in the tuple? "))

temp_list = []
for i in range(n):
    value = input("Enter element: ")
    temp_list.append(value)

my_tuple = tuple(temp_list)

print("Tuple =", my_tuple)


n = int(input("How many key-value pairs? "))

my_dict = {}
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    my_dict[key] = value

print("Dictionary =", my_dict)


n = int(input("How many elements in the set? "))

my_set = set()
for i in range(n):
    value = input("Enter element: ")
    my_set.add(value)

print("Set =", my_set)
