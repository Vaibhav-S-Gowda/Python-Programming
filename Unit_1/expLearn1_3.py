# Read N words; use defaultdict(list) to group anagrams. Print only groups with size ≥ 3.



from collections import defaultdict

# Step 1: Create a defaultdict where each key maps to a list
anagrams = defaultdict(list)

# Step 2: Read N (number of words)
n = int(input("Enter number of words: "))

# Step 3: Take N words as input and group them
for i in range(n):
    word = input(f"Enter word {i + 1}: ").strip()
    
    # Step 3a: Sort the letters in the word to form a key
    key = ''.join(sorted(word))
    
    # Step 3b: Add the word to the corresponding group
    anagrams[key].append(word)

# Step 4: Print only groups that have 3 or more anagrams
print("\nAnagram groups with 3 or more words:\n")
found = False
for group in anagrams.values():
    if len(group) >= 3:
        print(group)
        found = True

if not found:
    print("No groups found with 3 or more anagrams.")
