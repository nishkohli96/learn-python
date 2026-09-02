# For more, refer Notes.md

import json

json_file = "./assets/user.json"
json_file_write = "./assets/user_new.json"

try:
    with open(json_file) as file:
        # user is a python dictionary, if valid json
        user = json.load(file)
except FileNotFoundError:
    print(f"{json_file} not found.")
    user = None
# raises json.JSONDecodeError if malformed
except json.JSONDecodeError as e:
    print(f"Invalid JSON in {json_file}: {e}")
    user = None

print(user)

if user is not None:
    user["city"] = "New Delhi"

    with open(json_file_write, "w") as file:
        json.dump(user, file, indent=2)
    print(user)
