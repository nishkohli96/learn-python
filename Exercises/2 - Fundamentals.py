# 1. Write a function that accepts any number of integers and returns their average.

def avg_of_numbers(*nums):
    return sum(nums) / len(nums)


# OR
avg_lambda = lambda *x: sum(x) / len(x)

print(avg_of_numbers(1, 2, 3, 4, 5))
nums = [12, 22, 23, 44, 55]
# Unpack the list while calling the function
print(avg_of_numbers(*nums))

# 2. Write a function that accepts any number
# of keyword arguments and prints them as "key: value"

def print_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_args(name="Tom", age=24)

# 3. Write a lambda that returns the larger of two numbers.
# Basic -> largest_num = lambda a, b: a if a > b else b
largest_num = lambda a, b: max(a, b)
largest_num_from_list = lambda *nums: max(nums)

print(largest_num(34, 32))
print(largest_num_from_list(23, 1, 34, 45, 25))

# 4. Sort this list by age using a lambda:
people = [
    {"name": "Nishant", "age": 30},
    {"name": "Amit", "age": 25},
    {"name": "Rahul", "age": 28},
]

sorted_people = sorted(people, key=lambda person: person["age"])
print(sorted_people)
