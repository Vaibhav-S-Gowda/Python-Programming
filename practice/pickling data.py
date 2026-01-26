import pickle

# 1. The data we want to save
user_data = {
    "name": "Alice",
    "level": 42,
    "inventory": ["sword", "shield", "potion"],
    "is_active": True
}

# 2. Pickling: Writing the object to a file
# 'wb' stands for "write binary"
with open("data.pkl", "wb") as file:
    pickle.dump(user_data, file)
    print("Data has been successfully pickled and saved to data.pkl")

# 3. Unpickling: Reading the object back from the file
# 'rb' stands for "read binary"
with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)

print("\nData retrieved from pickle file:")
print(loaded_data)
print(f"Type of loaded data: {type(loaded_data)}")