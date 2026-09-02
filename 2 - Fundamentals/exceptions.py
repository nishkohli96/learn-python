# An exception is an error that occurs while the program is running.

print("Start")
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero.")
print("End")

numbers = [10, 20]
try:
    print(numbers[10])
except IndexError:
    print("Invalid index.")

print("--- Multiple Exceptions ---")

# Multiple Exceptions
# Shortcut
# try:
#    ...
# except (ValueError, TypeError):
#    print("Invalid input.")
try:
    x = int(input("Enter number: "))
    print(10 / x)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Zero is not allowed.")

# Getting the Actual Error
try:
    print(20 / 0)

except ZeroDivisionError as error:
    print(error)  # division by zero

try:
    numbers = [1]
    print(numbers[5])
except IndexError as error:
    print(error)  # list index out of range

# Else: else runs only if no exception occurred!
try:
    number = int(input("number: "))
except ValueError:
    print("Invalid")
else:
    print(number * 2)

# Finally
# finally always runs whether:
# - no error
# - error
# - return
# - break

# try:
#     print(10 / 0)
# finally:
#     print("Cleaning up...")

# Raising Own Exceptions
age = -5
if age < 0:
    raise ValueError("Age cannot be negative.")

password = "123"
if len(password) < 8:
    raise ValueError("Password too short.")

# Just subclassing Exception with pass is enough to get a distinct,
# catchable exception type — you don't need to add anything else
# for it to work.
class NoFundsError(Exception):
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise NoFundsError("Not enough balance to withdraw")
    return balance - amount


withdraw(100, 150)

try:
    int("abc")
except ValueError as error:
    raise RuntimeError("User input failed") from error
# Output - RuntimeError: User input failed

person = {"name": "Alice", "age": 30}
try:
    person["city"]
except KeyError as e:
    print(f"Missing key: {e}")
    # Missing key: 'city'