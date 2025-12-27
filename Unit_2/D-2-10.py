class MathHelper:
    ''' A Utility class providing static methhods for mathematical operations.'''
    @staticmethod
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
            
        for i in range(2, n):
            if n % i == 0:
                return False
                
        # If the loop completes without finding any divisors, the number is prime
        return True
        
test_numbers = [
    1,2,3,45,6,7,
    11,15,17,21,29,
    97,100,121
]

print("--- Prime Nummber Checker Results (Basic) ---")
print("{:<10} | {:<10}".format("Number", "Is Prime?"))
print("-" * 25)

for number in test_numbers:
    # Call static method directly on the class
    is_prime_result = MathHelper.is_prime(number)
    print("{:<10} | {:<10}".format(number, is_prime_result))