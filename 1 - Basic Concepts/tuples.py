# tuple: (), immutable — fix after create, no change allowed.
# tuple usable as dict key / set member (hashable), list not.
# Use tuples when data shouldn't change.
# tuple are not same as enum. tuple just fix-value container,
# no name-to-value mapping, no type safety.

coordinates = (10, 20)
print(coordinates[0])

# TypeError: 'tuple' object does not support item assignment
# If I try to change the value of a tuple, it will throw an error.
# coordinates[0] = 50

months = ("Jan", "Feb", "Mar")

accept = ['.png', '.jpg']
file_name = "photo.png"

is_valid = file_name.lower().endswith(tuple(accept))
# True

# If you actually want the matched extension itself (true Array.find() equivalent):
matched = next((ext for ext in accept if file_name.lower().endswith(ext)), None)

# ext in accept
# Say if u already have file extension and want to check
# if it is allowed