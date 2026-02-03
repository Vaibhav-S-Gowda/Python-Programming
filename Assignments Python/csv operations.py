import csv, os

# Opening a csv file
def open_csv():
    with open("Assignments Python/resources/data.csv", mode="r") as file:
        content = file.read()
        print(content)

def read_csv():
    with open("Assignments Python/resources/data.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")

        rows = list(reader) 
        print(rows)

def csv_dictReader():
    with open("Assignments Python/resources/data.csv", "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            print(row)
        
        print(row["Name"])
        print(row["City"])

def write_csv():
    with open("Assignments Python/resources/output.csv", "w") as f:
        writer = csv.writer(f)

        writer.writerow(["Name", "Age", "City"])
        writer.writerow(["John", "29", "Agra"])

def write_multiple_rows():
    with open("Assignments Python/resources/output.csv", "r+", newline = "") as f:
        writer = csv.writer(f)

        data = [
            ["Alice", 22, "Bangalore"],
            ["Nithya", 22, "Bangalore"],
            ["Atharva", 25, "Mysore"]
        ]
        writer.writerows(data)

def csv_dictWriter():
    with open("Assignments Python/resources/students.csv", "w", newline="") as f:
        filednames = ["Name", "Age", "City"]
        writer = csv.DictWriter(f, fieldnames=filednames)

        writer.writeheader()
        writer.writerow({"Name": "Alice", "Age": 22, "City": "Bangalore"})

def appending_data_existing_csv():
    with open("Assignments Python/resources/students.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['Charlie', 28, "Chennai"])

def counting_rows():
    with open("Assignments Python/resources/data.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        count = sum(1 for row in reader)
        print(count)

def deleting_row():
    with open("data.csv", "r") as f:
        reader = csv.reader(f)
        rows = [row for row in reader if row[0]!= "Dean"]
        print(rows)

def sorting_data():
    with open("Assignments Python/resources/output.csv", "r") as f:
        reader = csv.reader(f)
        for rows in reader:
            rows.sort(key=lambda x: x[1])
        print(rows)

if __name__ == "__main__":
    sorting_data()