try:
    f = open('new.txt', 'r')
    print('File Opened')
except IOError as e:
    print(f'IOError: {e}')