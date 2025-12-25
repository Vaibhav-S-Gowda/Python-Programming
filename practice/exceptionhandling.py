print('Execution started normally')
lst = [10, 20, 0, 40, 50]
d = {1:'c', 2:'java', 3:'python', 4:'c++'}

try:
    r = int(input('Enter the rank of the language: \n'))
    print(d[r])
    num = int(input('Enter the index of numerator'))
    den = int(input('Enter the index of denominator'))
    print(lst[num/lst[den]])
except KeyboardInterrupt as e:
    print(f'{e} occured')
except KeyError as e:
    print(f'Key does not exist: {e}')
except IndexError as e:
    print('Index out of bound')
except ZeroDivisionError:
    print('Division by zero', ZeroDivisionError)
finally:
    print('Execution terminated normally')
