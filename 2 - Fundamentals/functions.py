# As per convention, it is recommended to add 2 line breaks
# when calling a function after defining it
#
# "None" is returned if there is no return value from a function call

# Every Python file (module) has a __name__ variable automatically
# set by the interpreter:
# - If you run the file directly (python script.py),
#   Python sets __name__ = "__main__" for that file.
# - If you import the file as a module into another file,
#   Python sets __name__ to the module's filename (without .py).
print(__name__) 

# Best Practices
# - Keep functions focused on one job.
# - Return values instead of printing them.
# - Use descriptive names like calculate_total() instead of calc().
# - Prefer keyword arguments for functions with many optional parameters.
# - Use *args and **kwargs only when flexibility is genuinely needed.
# - Add type hints and docstrings in production code.
# - Avoid mutable default arguments.


# 1: Basic Functions
def greet():
    print("Hello world")


greet()


# 2: Function with args and return value
def print_name(first_name, last_name):
    return f"Hello {first_name} {last_name}"


print(print_name("John", "Doe"))


# 3: Recursive Functions
def get_factorial(num):
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if num == 0 or num == 1:
        return 1
    return num * get_factorial(num - 1)


test_num = 5
print(f"{test_num}! = {get_factorial(test_num)}")

# To make function call more easier, we can also add argName(s) alongside
# values when calling a function.
print(get_factorial(num=7))


# 4: Functions with optional args
# For optional args, ensure that they always have a default value,
# else we get a runtime error that the function requires 2 args in this case
#
# All the OPTIONAL params must always come after REQUIRED params
def increment_num(num, by=1):
    return num + by


print("increment_num(5)", increment_num(5))
print("increment_num(12, 3)", increment_num(12, 3))


# 5: Functions with variable args
# In this case, user "*" before arg name, indicating the function can
# have variable args. Also prefer plural name for arg in this case
def multiply_nums(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


print(multiply_nums(2, 3))
print(multiply_nums(4, 6, 8, 10, 3))


# 6. Function returning a tuple
def calculate(a, b):
    return a + b, a - b


result = calculate(10, 3)
print(result)
print(type(result))

# Combining two operations in a single function
sum_value, difference = calculate(10, 3)
print(sum_value)
print(difference)


# 7. Function with default args
# def increment(num, by=1):
#     return num + by
# A function can have multiple default args
def create_user(name, age=18, city="Delhi"):
    print(name, age, city)


create_user("Raj")
# To skip an optional parameter and use its default value,
# use keyword arguments for the parameters that follow.
# If I wrote "city1" instead of "city", it would throw error.
create_user("Amit", city="Lucknow")

# 8. Keyword Arguments
# Instead of create_user("Nishant", 30, "Delhi"), use
create_user(city="Delhi", age=30, name="Ollie")

# Not allowed - create_user(city="Delhi","Nishant")
# Keyword arguments must come after positional arguments.


# 9. Variable args
def printargs(*args):
    print(args)


printargs(2)  # (2,) ie. a tuple
printargs(2, 3, 4)  # (2, 3, 4)


def addition(*numbers):
    return sum(numbers)


print(addition(2, 3))
print(addition(2, 3, 4))
print(addition(2, 3, 4, 5))

# 10. Common mistake -
# def add_item(item, items=[]):
#     items.append(item)
#     return items
# The same list is reused across calls.
#
# Correct way ->
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items

print("--- End of program ---")
