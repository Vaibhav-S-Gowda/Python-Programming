def create_file(filepath):
    open(filepath, 'x') # creates a file if it does not exists
    print(f'{filepath} created successfully')

create_file('new_file1.txt') # FileExistsError: [Errno 17] File exists: 'new_file1.txt'