# 1. Reverse a list using slicing.
names = ["raj", "amit", "suresh"]
reverse_names = names[::-1]
print(reverse_names)

# 2. Find the largest number in a list.
nums = [12, 45, 3, 52, 34]
print(max(nums))

# 3. Remove duplicates from a list using a set.
dups_list = [2, 4, 1, 2, 5, 2, 1]
numbers_set = set(dups_list)
print(numbers_set)

# 4. Count how many times each word appears in a sentence using a dictionary.
sample_str = "He is the chief of the staff of his chief."
word_count = {}
for word in sample_str.lower().replace(".", "").split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)

# Instead of
#   if word not in dict:
# you can simply do
#   dict[word] = dict.get(word, 0) + 1
#
# Even more Pythonic:
#   from collections import Counter
#   word_count = Counter(sample.lower().replace(".", "").split())

# 5. Create a list of squares from 1–20 using a list comprehension.
sq_list = [x**2 for x in range(1, 21)]
print(sq_list)

# 6. Create a dictionary mapping numbers 1–10 to their cubes using a dictionary comprehension.
cube_dict = {x: x**3 for x in range(1, 11)}
print(cube_dict)

# 7. Swap two variables without using a third variable.
var1 = "Hello"
var2 = "World"
var1, var2 = var2, var1

# 8. Given a nested dictionary of students and marks, print the average marks for each student.
students = [
    {"name": "Nishant", "marks": [90, 88, 95]},
    {"name": "Rahul", "marks": [80, 75, 85]},
]

# solution 1
for student in students:
    average = sum(student["marks"]) / len(student["marks"])
    print(student["name"], average)

# Best solution
averages = {
    student["name"]: sum(student["marks"]) / len(student["marks"])
    for student in students
}
print(averages)