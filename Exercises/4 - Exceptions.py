# 1. Write a function that safely divides two numbers and
# returns "Cannot divide" if the denominator is zero.

def division(numerator, denominator):
    if denominator == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return numerator / denominator


try:
    result = division(10, 0)
    print(f"division result: {result}")
except ZeroDivisionError as e:
    print(e)
finally:
    print("division function executed")


# 2. Write a function that accepts a filename and handles FileNotFoundError.

def read_file(filename):
    try:
        with open(filename) as file:
            print(file.read())

    except FileNotFoundError:
        print("File not found.")

# Python looks in the current working directory, so if I input
# "Exercises/Exercise_Basic.py"
# it will print its contents, else throw exception 
file_name = input("Enter file name: ").strip()
try:
    read_file(file_name)
finally:
    print("file reading function executed")


# 3. Create a custom exception named InvalidSalaryError and
# raise it if the salary is negative.
class InvalidSalaryError(Exception):
    def __init__(self, salary: int):
        self.salary = salary
        super().__init__(f'The salary "{self.salary}" cannot be negative')


try:
    salary_str = input("Enter your monthly salary: ")
    salary = int(salary_str)
    if salary < 0:
        raise InvalidSalaryError(salary)
    print(f"You earn ${salary} per month")
except ValueError as v_err:
    print(f"Error: {v_err}")
except InvalidSalaryError as salary_err:
    print(f"Salary Error: {salary_err}")
