try:
    with open("new_file.txt",'r') as f:
        for line in f:
            line = line.strip()
            try:
                num = int(line)
                print("Converted: ",num)
            except ValueError as ve:
                print(f'{ve}: Cannot convert string to \
                      integer.',line)
except FileNotFoundError as fnfe:
    print(fnfe)