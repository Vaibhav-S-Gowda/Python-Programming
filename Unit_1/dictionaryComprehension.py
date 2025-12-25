# Syntax {key_exp : value_exp for item in iterable}

# ---------------- Simple Comprehension ----------------
even_squares = {x: x**2 for x in range(10)}
print(even_squares) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

d = {a: a+10 for a in range(5)}
print(d) # {0: 10, 1: 11, 2: 12, 3: 13, 4: 14}

# ---------------- Conditional Comprehension ----------------
d = {a: a**3 for a in range(10) if (a**3 % 4) == 0}
print(d) # {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}

# ---------------- Nested Comprehension ----------------
d = {a: {b: a+b for b in 'ABC'} for a in 'ABC'}
print(d) # {'A': {'A': 'AA', 'B': 'AB', 'C': 'AC'}, 'B': {'A': 'BA', 'B': 'BB', 'C': 'BC'}, 'C': {'A': 'CA', 'B': 'CB', 'C': 'CC'}}

# ---------------- Nested Conditional Comprehension ----------------
d = {x: {y: 'EVEN' if y%2 == 0 else 'ODD' for y in range(1,5)} for x in range(1,3)}
print(d) # {1: {1: 'ODD', 2: 'EVEN', 3: 'ODD', 4: 'EVEN'}, 2: {1: 'ODD', 2: 'EVEN', 3: 'ODD', 4: 'EVEN'}}
