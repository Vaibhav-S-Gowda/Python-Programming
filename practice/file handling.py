with open("practice.txt", "r") as f:
    data = f.read()

numbers = []
num = ""

for ch in data:
    if ch == ",":
        numbers.append(int(num))
        num = ""
    else:
        num += ch

# add the last number
numbers.append(int(num))

count = 0
for n in numbers:
    if n % 2 == 0:
        count += 1

print("Numbers:", numbers)
print("Even count:", count)
