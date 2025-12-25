# Read N integers; build OrderedDict to keep first occurrence only. Print unique sequence preserving input order

from collections import OrderedDict

# Step 1: Create an empty OrderedDict
unique_numbers = OrderedDict()

# Step 2: Read how many integers to input
n = int(input("Enter number of integers: "))

# Step 3: Read N integers one by one
for i in range(n):
    num = int(input(f"Enter integer {i + 1}: "))
    
    # Step 4: Add to OrderedDict only if not already present
    if num not in unique_numbers:
        unique_numbers[num] = True   # Value doesn't matter, only key matters

# Step 5: Print the unique sequence preserving the input order
print("\nUnique numbers (first occurrences only):")
for num in unique_numbers.keys():
    print(num, end=" ")
