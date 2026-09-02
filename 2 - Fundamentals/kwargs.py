# **kwargs lets a function accept any number of keyword
# arguments it wasn't explicitly designed for, collecting
# them into a dictionary.

# Whatever keyword arguments the caller passes get packed
# into a dict called kwargs (the name kwargs is just a
# convention — the ** is what matters, you could call it **anything).

def greet(**kwargs):
    print(kwargs)


greet(name="Alice", age=30, city="NYC")
# {'name': 'Alice', 'age': 30, 'city': 'NYC'}


# Why use it:
# 1. Flexible APIs — accept optional settings without
#    listing every possible one:
def create_user(name, **kwargs):
    email = kwargs.get("email", "not provided")
    role = kwargs.get("role", "user")
    print(f"{name}, {email}, {role}")


create_user("Bob", email="bob@x.com", role="admin")
create_user("Amy")  # optional kwargs just omitted


# 2. Passing arguments through to another function
#    (very common in wrappers/decorators):


def example(a, b, *args, **kwargs):
    print(a, b, args, kwargs)


example(1, 2, 3, 4, x=5, y=6)
# 1 2 (3, 4) {'x': 5, 'y': 6}


# Unpacking a dict into a call (the reverse direction):
def greetWithAge(name, age):
    print(f"{name} is {age}")


params = {"name": "Alice", "age": 30}
greetWithAge(**params)  # unpacks dict into name=..., age=...
