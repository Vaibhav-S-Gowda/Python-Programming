# Import Counter class from collections module
from collections import Counter

# Step 1: Ask user to enter a string
user_input = input("Enter a string: ")

# Step 2: Create a Counter object to count each character
# Counter works like a dictionary where:
#   key   = character
#   value = how many times that character appears
character_count = Counter(user_input)
print(f'{character_count}')
print("\nCharacters that appear more than 2 times:\n")

for character in character_count:
    count = character_count[character]  # get frequency of that character
    
    if count > 1:
        print(f"The character '{character}' appears {count} times.")
