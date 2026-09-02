# A decorator is a function that takes another function,
# adds/modifies behavior, and returns a new function.

# Decorators can also be stacked
# @decorator1
# @decorator2
# def greet():
#     print("Hello")

import time
from functools import wraps


def log_function(func):
    def wrapper():
        print(f"Calling {func.__name__}")
        func()
        print(f"Finished {func.__name__}")

    return wrapper


@log_function
def login():
    print("User logged in")


login()


# Decorator with args
# Why *args and **kwargs?
# The decorator doesn't know what arguments the function will eventually require.
# So:
#   def wrapper(*args, **kwargs)
# captures everything.
def log_function_args(func):

    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result

    return wrapper


@log_function_args
def greet(name):
    print(f"Hello {name}")


greet("Rajesh")


def timer(func):

    # Decorator to preserve metadata such as: __name__, __doc__
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result

    return wrapper


@timer
def expensive_operation():
    time.sleep(2)
    return "Done"


result = expensive_operation()
