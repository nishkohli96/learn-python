import json
import csv
from pathlib import Path


# 1. Create a file named hello.txt and write "Hello Python" into it

assets_dir = Path(__file__).resolve().parent / "../assets"
hello_python = assets_dir / "hello-python.txt"

with open(hello_python, "w") as file:
    file.write("Hello Python")

# 2. Read users.txt and print each line without extra blank lines.
with open(assets_dir / "users.txt") as users_file:
    for line in users_file:
        print(line.strip())

# 3. Append "Learning Python" to "hello-python.txt".
with open(hello_python, "a") as file:
    file.write("\nLearning Python\n")

# 4. Create and save "user" in user_created.json.
user = {"name": "Nishant", "age": 30}
with open(assets_dir / "user_created.json", "w") as json_file:
    json.dump(user, json_file, indent=2)

# 5. Read user.json and print "Nishant is 30 years old"
try:
    with open(assets_dir / "user.json") as user_file:
        user = json.load(user_file)
        print(f"{user['name']} is {user['age']} years old")
except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError as e:
    print(f"Invalid JSON in {assets_dir / 'user.json'}: {e}")

# 6. Read "employees.csv" using DictReader and print: "X earns Y"
try:
    with open(assets_dir / "employees.csv") as employees_file:
        csv_reader = csv.DictReader(employees_file)
        for row in csv_reader:
            print(f"{row['name']} earns {row['salary']}")
except FileNotFoundError:
    print("File not found")
