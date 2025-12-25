try:
    data = input("Enter something to write into the file: ")

    with open("new_file.txt", "w") as f:
        f.write(data)
        print("Data written successfully.")

except PermissionError:
    print("Error: You don't have permission to create or write to this file.")
