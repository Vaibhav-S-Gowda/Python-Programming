# ---------------- Simple Comprehension ----------------
s = {a for a in range(10)}
print(s) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

s = {a*2 for a in range(10)}
print(s) # {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}

# ---------------- Conditional Comprehension ----------------
s = {a*2 for a in range(10) if( a%2 == 0)}
print(s) # {0, 4, 8, 12, 16}

s = {a+2 for a in range(10) if a%2 != 0}
print(s) # {3, 5, 7, 9, 11}

# ---------------- Nested Comprehension ----------------
s = {a*b for a in range(1,5) for b in range(1,3)}
print(s) # {1, 2, 3, 4, 6, 8}

s = {(a,b) for a in [1,2,3,4,5] for b in ['a','b','c']}
print(s) # {(4, 'b'), (1, 'a'), (2, 'b'), (4, 'c'), (3, 'b'), (4, 'a'), (5, 'b'), (2, 'c'), (1, 'b'), (3, 'c'), (2, 'a'), (5, 'a'), (3, 'a'), (5, 'c'), (1, 'c')}

# ---------------- Nested Conditional Comprehension ----------------
s = {a*b for a in range(10) for b in range(5) if (a + b)%2 == 0}
print(s) # {0, 1, 32, 3, 4, 5, 7, 8, 9, 12, 15, 16, 21, 24, 27}

s = {(a,b) for a in [1,2,3,4] for b in [4,5] if (a + b)%2 == 0}
print(s) # {(4, 4), (2, 4), (3, 5), (1, 5)}