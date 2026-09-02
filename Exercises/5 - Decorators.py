from functools import wraps


# 1. Logging decorator
def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@log_call
def greet(name):
    return f"Hello {name}"


print(greet("Tanmay"))


# 2. Positive numbers decorator
def positive_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        number = args[0]
        if number < 0:
            raise ValueError("Negative numbers are not allowed")
        return func(*args, **kwargs)

    return wrapper


@positive_only
def square(number):
    return number**2


print(square(5))

try:
    print(square(-5))
except ValueError as verr:
    print(verr)


# 3. Repeating Decorator
def repeat(num):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                func(*args, **kwargs)
        return wrapper
    return decorator

# equivalent to hello = repeat(3)(hello)
@repeat(3)
def hello():
    print("Hello")


hello()
