n = int(input("Enter the numerator: "))
try:
    d = int(input("Enter the denominator: "))
    print(n/d)
except:
    print("Error: Denominator cannot be a zero")
finally:
    print("Division may have occurred")
    ''' finally block is executed if the exception is identifed and handled
        finally block is executed if the exception does not occur also'''