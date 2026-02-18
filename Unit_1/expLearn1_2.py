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
    

'''
    Core Flow
        Collects 10 user inputs into a list
        Uses Counter to compute item occurrence frequency
        Determines maximum frequency using max()
        Filters and prints item(s) matching highest occurrence (supports ties)

    Technical Highlights
        Efficient built-in frequency computation
        Linear time complexity → scalable for larger datasets
        Handles duplicate detection cleanly

    Scope for Enhancement
        Dynamic input size
        Input normalization (case handling)
        Input validation
        Persistence (file/database storage)

    Use Case
        Applicable in basic demand analysis, log frequency detection, and simple data analytics pipelines.
'''