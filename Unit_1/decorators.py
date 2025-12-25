def div(x, y):
    print(x / y)

# ----------------- Wrapper Function -----------------
def check(f):
    def value(x, y):
        if x < y:
            x,y = y,x
            return f(x,y)
        return f(x,y)
    return value
df = check(div)
df(10, 12) # 1.2

# ----------------- Syntatic Decorators -----------------

def split_val(f):
    def val():
        func = f()
        s_s = func.split()
        return s_s
    return val

def upper_val(f):
    def val():
        func = f()
        u_v = func.upper()
        return u_v
    return val

# Applying decorators on the normal function
@upper_val
def input_val():
    return 'This is Python program.'
print(input_val()) # Calling function

@split_val
def input_val():
    return 'This is Python program.'
print(input_val()) # Calling function

# Applying Single Decorator On Functions That can Take Parameters Or On Functions That Do Not take Parameters
# -----------------------------------------------------------------------------------------------------------
# Wrapper Function
def dec(f):
    def wrap(*args, **kwargs):
        print(f'The positional arguments are {args}')
        print(f'The keywords arguments are {kwargs}')
        f(*args)
    return wrap

# Apply the decorator on a function that takes no parameter
@dec
def func_no():
    print('No Arguments passed')
print(func_no())

# Apply the decorator on a function that takes positional arguments
@dec
def f_pos(a,b,c):
    print(f'The parameters are {a}, {b}, {c}')
print(f_pos(1,2,3))

# Apply the decorator on a function that takes Keyword arguments
@dec
def f_key():
    print('The function takes keyword arguments')
print(f_key(f_name = 'Harry', l_name = 'Potter', age = 11))
