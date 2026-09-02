person = {
    "name": "Niko",
    "age": 30,
    "city": "Delhi"
}
print(person)

# Accessing a key
print(person["name"])

# Modifying a key
person["age"] = 41
print(person)

# Getting a key, if key not found, return default value
person_name = person.get("name1", "N/A")
print(f"person_name: {person_name}")

# Append a new key-value pair
person["salary"] = 50000
print(person)

# Deleting a key-value pair
del person["city"]
print(person)

# Iterating over keys
for key in person:
    print(key)

# Iterating over values
for value in person.values():
    print(value)

# Iterating over key-value pairs
for key, value in person.items():
    print(key, value)

# Output: {6: None, 1: None, 2: None, 3: None, 4: None}
print(dict.fromkeys([6, 1, 2, 3, 3, 1, 4, 2]))
