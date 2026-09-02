# For more, refer Notes.md

import csv

csv_file = "./assets/students.csv"

# Reads each row as a list
try:
    with open(csv_file) as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print(f"{csv_file} not found.")
except csv.Error as e:
    print(f"CSV parsing error: {e}")

# Reads each row as a dictionary
#
# print(row["age"]) if "age" doesnt exist will give KeyError
# age = row.get("age")
# if age is None:
#     print("Age not provided")

with open(csv_file) as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)

# Appending to a CSV file
with open(csv_file, "a", newline="") as file:
    writer = csv.writer(file)
    # If I were to overwrite this file, "w" instead of
    # "a", and uncomment below line 
    # writer.writerow(["name", "marks"])
    writer.writerow(["Rajat Kumar", 75])