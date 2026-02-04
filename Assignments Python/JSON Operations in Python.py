import json

filename = "Assignments Python/resources/data.json"

def load_json_file():
    with open(filename, "r") as f:
        data = json.load(f)

    print(data)
    print(type(data))

def access_like_dict():
    with open(filename, "r") as f:
        data = json.load(f)
    
    print(data["name"])
    print(data["skills"])
    print(data["skills"][0])

def modify_existing_json_values():
    with open(filename, "r") as f:
        data = json.load(f)
        data["age"] = 23
        print(data)

def add_new_key_pair_value():
    with open(filename, "r") as f:
        data = json.load(f)
        data["email"] = "alice@gmial.com"
        print(data)

def delete_key():
    with open(filename, "r") as f:
        data = json.load(f)
        del data["city"]
        print(data)

def add_items_inside_json_array():
    with open(filename, "r") as f:
        data = json.load(f)
        data["skills"].append("Machine Learning")

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print("Skill added permanently!")
    print(data["skills"])

def remove_items_from_json_array():
    with open(filename, "r") as f:
        data = json.load(f)
        data["skills"].remove("SQL")
        print(data["skills"])

def python_dict_to_json_string():
    with open(filename, "r") as f:
        data = json.load(f)
    
        json_string = json.dumps(data, indent=4)
        print("JSON String:\n", json_string)
        print("Type: ", type(json_string))

    with open(filename, "w") as f:
        f.write(json_string)

def convert_json_string_to_python_object():
    with open("Assignments Python/resources/broken.json", "r") as f:
        text = '{"name": "Marly", "age": 25}'
        obj = json.loads(text)
        print(obj)
        print(type(obj))
        # with open(filename, "w") as f:
        #     json.dump(obj, f, indent=4)

def handle_invalid_json():
    try:
        with open("Assignments Python/resources/broken.json") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("Invalid JSON format!")

if __name__ == "__main__":
    convert_json_string_to_python_object()