def fun2():
    print('fun2() started execution')
    try:
        num = int(input('Enter the numerator: '))
        den = int(input('Enter the denominator: '))
        res = num/den
        print(res)
    except ZeroDivisionError as e:
        print(f'{e} : Exception handled in fun2()')
    print('fun2() finished execution normally')

def fun1():
    print('fun1() started execution')
    try:
        fun2()
    except ValueError as e:
        print(f'Provide the appropriate value : {e}')
        print('Exception handled in fun1()')
    print('fun1() finished execution normally')

def main():
    try:
        print('main() started execution') 
        fun1()
    except KeyboardInterrupt as e:
        print(f'Unknown key pressed: {e}')

    print('main() finished execution normally')
main()