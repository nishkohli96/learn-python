# A set stores unique values only.

# {1, 2, 3, 4, 6}
# Duplicates disappear automatically.
numbers = {6, 1, 2, 3, 3, 1, 4, 2}
print(numbers)

# Adding an item to a set.
numbers.add(9)
print(numbers)

# Removing an item from a set.
numbers.remove(2)
print(numbers)

# Checking if an item exists in a set.
if 3 in numbers:
    print("Found: 3")
print(5 in numbers) # False

print("length of numbers: ", len(numbers))

original_numbers = list(dict.fromkeys([6, 1, 2, 3, 3, 1, 4, 2]))
print(original_numbers)  # [6, 1, 2, 3, 4]