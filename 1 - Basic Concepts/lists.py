# A list is an ordered collection of items.
# list: [], mutable — add/remove/change item after create.
# list slower, tuple faster (lighter, less overhead).

fruits = ["apple", "banana", "orange"]
print("fruits: ", fruits)

# Length of the list.
print("length of fruits: ", len(fruits))

# Lists can store different data types.
data = ["Joe", 30, True, 95.5]
print("data: ", data)

# Index starts from 0.
print(fruits[0])

# Negative indexes start from the end.
print(fruits[-1])

# Updating a list item.
fruits[1] = "mango"
print(fruits)

# Adding items
# append() - Adds to the end.
fruits.append("kiwi")
print(fruits)

# Insert item at a specific index, shifts the rest of the items to the right.
fruits.insert(1, "grapes")
print(fruits)

# Removing items
# Remove specific item by value
fruits.remove("apple")
print(f"after removing \"apple\": {fruits}")

# Throws error if item not found, thus we can use try-except block to handle it.
try:
    fruits.remove("muskmelon")
except ValueError:
    print("Item not found in the list.")

# Remove last item
popped = fruits.pop()
print("Removed item: ", popped)
print(f"after pop(): {fruits}")

# Slicing a list
# list[start:end]
# end index is exclusive, thus it will not include the item at end index.

# Even though size of list is 3, it will not throw error if index is out of range
print(fruits[0:6])

# IndexError: list index out of range
# print(fruits[5]) 

nums = [10,20,30,40,50]
print(nums[2:])

# Everything before index 3
print(nums[:3])

# Copying a list
# changes in original list will NOT reflect in the copied list.
nums_duplicate = nums[:]
nums[2] = 100
print("nums: ", nums)
print("nums_duplicate: ", nums_duplicate)

# Slicing with step
nums_step = nums[::2]
print("nums_step: ", nums_step)

# Reverse copy
nums_reverse = nums[::-1]
print("nums_reverse: ", nums_reverse)

# Sorting a list
nums_unsorted = [5,2,7,1]

# Reverse a list
nums_unsorted.reverse()
print(f"After reversing: {nums_unsorted}")

# sorted() - Returns new list
new_nums = sorted(nums_unsorted)
print("new_nums: ", new_nums)

# mutates the original list
nums_unsorted.sort(reverse=True)
print("nums_reverse_sorted: ", nums_unsorted)

# Sorting a list of strings
names = ["John", "Amy", "Bob"]
names.sort()
print("names_sorted: ", names)

# Join two lists
# nums_unsorted = [7, 5, 2, 1, 'Amy', 'Bob', 'John']
nums_unsorted.extend(names)
print("nums_unsorted: ", nums_unsorted)

# Collections can contain other collections.
students = [
    {
        "name": "Raj",
        "marks": [90, 88, 95]
    },
    {
        "name": "Rahul",
        "marks": [80, 75, 85]
    }
]

print(type(students))
print(students[0]["marks"][2])

names = ["Raj", "Amit", "Rahul"]
ages = [25, 30, 28]

# zip():
# - combine sequences
# - normally stops when the shortest iterable is exhausted.
for name, age in zip(names, ages):
    print(name, age)


# map() — transform every element
numbers = [1, 2, 3, 4]
squares = map(lambda x: x ** 2, numbers)

# any() — does at least one satisfy the condition?
print(any(x % 2 == 0 for x in numbers))

# all() — do all satisfy the condition?
numbers_even = [2, 4, 6, 8]
print(all(x % 2 == 0 for x in numbers_even))

# min() — smallest value, works for numbers and strings
numbers = [10, 4, 25, 2, 18]
print(min(numbers))

names = ["Raj", "Amit", "Suresh"]
print(min(names)) # Amit

# max() — largest value
people = [
    {"name": "Nishant", "age": 30},
    {"name": "Amit", "age": 25},
    {"name": "Rahul", "age": 35},
]

oldest = max(people, key=lambda person: person["age"])
print(oldest)
