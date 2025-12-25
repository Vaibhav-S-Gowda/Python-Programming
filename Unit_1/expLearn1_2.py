# Using a loop, collect 10 shopping items as input. 
# Use a Counter to count occurrences and display the most common item. 
# If there’s a tie, display all tied items.

from collections import Counter

ShoppingItems = []

for i in range(0,10):
    items = input("Enter shopping item: ")
    ShoppingItems.append(items)
    
freq = Counter(ShoppingItems)
max_count = max(freq.values())
print("Items which have occured more frequently: ")

for item,count in freq.items():
    if count == max_count:
        print(f"'{item} appears {count} times")
    