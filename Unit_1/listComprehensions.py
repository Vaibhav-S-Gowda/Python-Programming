# ---------------- Simple Comprehension ----------------
l = [a for a in range(10)]
print(l) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

l = [a*2 for a in range(10)]
print(l) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# ---------------- Conditional Comprehension ----------------
l = [a*2 for a in range(10) if( a%2 == 0)]
print(l) # [0, 4, 8, 12, 16]

# ---------------- Nested Comprehension ----------------
l = [a*b for a in range(1,5) for b in range(1,3)]
print(l) # [1, 2, 2, 4, 3, 6, 4, 8]

# ---------------- Nested Conditional Comprehension ----------------
l = [a*b for a in range(10) for b in range(5) if (a + b)%2 == 0]
print(l) # [0, 0, 0, 1, 3, 0, 4, 8, 3, 9, 0, 8, 16, 5, 15, 0, 12, 24, 7, 21, 0, 16, 32, 9, 27]


