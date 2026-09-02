# Instead of
# for x in range(1, limit + 1):
#    yield x
# Use:
# yield from range(1, limit + 1)

def count_up(limit):
    current = 1

    while current <= limit:
        yield current
        current += 1


counter = count_up(3)


def infinite_numbers():
    number = 1

    while True:
        yield number
        number += 1


numbers = infinite_numbers()

print(next(numbers))
print(next(numbers))
print(next(numbers))


users = [
    {"name": "Nishant", "active": True},
    {"name": "Rahul", "active": False},
    {"name": "Amit", "active": True},
]

# list
active_users_list = [user for user in users if user["active"]]

# generator
active_users = (user for user in users if user["active"])

# The generator approach is useful when the source dataset is very large.
for user in active_users:
    print(user)

# For a large file generate a function, which yields only
# lines containing "ERROR" without loading the entire file into memory.
# def read_large_file(filepath):
#     with open(filepath) as f:
#         for line in f:
#             yield line.strip()

# # Process a 10GB log file without ever holding it all in RAM
# for line in read_large_file("huge_server.log"):
#     if "ERROR" in line:
#         print(line)
