try:
    with open("new_file12345.txt",'r') as f:
        lines = f.readlines()

        if not lines:
            raise ValueError("The file is empty.")
        
        for i in range(min(5, len(lines))):
            print(lines[i].strip())

except FileNotFoundError as fnfe:
    print(fnfe)

except ValueError as e:
    print("Error:", e)