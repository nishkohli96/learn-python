# Context Managers

A context manager handles setup and cleanup of a resource automatically.

**Context Manager = Setup + Cleanup**

- Decorator → wraps a FUNCTION
- Context Manager → wraps a BLOCK OF CODE

```py
with open("data.txt") as file:
    content = file.read()
```
The `with` statement is using a context manager.

A context manager generally implements:

```py
__enter__()
__exit__()
```

## __enter__

`__enter__` runs when Python enters the `with` block. Its return value is assigned to the variable after `as`.

For example:

```py
with MyContext() as ctx:
    ...
```

is conceptually:

```py
ctx = MyContext().__enter__()
```

## __exit__

`__exit__` runs when Python leaves the `with` block. It runs even when an exception occurs.

```py
def __exit__(self, exc_type, exc_value, traceback):
    ...
```

These parameters describe an exception if one occurred.

If everything succeeds:

```py
exc_type   = None
exc_value  = None
traceback  = None
```

If something fails:

```py
exc_type   = exception class
exc_value  = exception instance
traceback  = traceback information
```

`__exit__` returns either: `True` or `False`

The exception is considered handled.

```py
def __exit__(self, exc_type, exc_value, traceback):
    return True
```

The program can continue to execute when retuned `True`.

```py
with MyContext():
    raise ValueError("Oops")

print("Program continues")
```

## Mental Model

```py
with MyContext():
    do_something()
```

is conceptually similar to:

```py
context = MyContext()

try:
    context.__enter__()
    do_something()
finally:
    context.__exit__(...)
```

## contextlib

Python provides a much easier way to create context managers.

Instead of defining a class with:

```py
__enter__
__exit__
```

you can use:

```py
from contextlib import contextmanager
```

Example:

```py
from contextlib import contextmanager


@contextmanager
def my_context():
    print("Enter")

    yield

    print("Exit")
```

Then:

```py
with my_context():
    print("Inside")
```

`yield` is the middle of the context, so

```py
print("Before")

    ↓ yield

print("Hello")

    ↓ resume generator

print("After")
```

### Returning a value from a Context Manager

```py
from contextlib import contextmanager

@contextmanager
def database_connection():
    print("Connecting...")
    connection = "DB Connection"
    yield connection
    print("Closing connection...")


with database_connection() as db:
    print(db)
```

### Handling Exceptions with `contextmanager`

You can use `try`/`finally` around the `yield`.

```py
from contextlib import contextmanager

@contextmanager
def resource():
    print("Opening resource")
    try:
        yield
    finally:
        print("Closing resource")

with resource():
    print("Doing work")
    raise ValueError("Oops")
```

Even though the exception occurs, the cleanup still happens.

### Real World Example

Imagine a database transaction.

```py
@contextmanager
def transaction(db):
    try:
        yield db     # transaction work happens here
        db.commit()  # commit AFTER the work

    except Exception:
        db.rollback()
        raise
```

Then:

```py
with transaction(db) as connection:
    create_user()
    create_order()
```

If everything succeeds:

```py
create_user()
     ↓
create_order()
     ↓
commit()
```

If something fails:

```py
create_user()
     ↓
create_order()
     ↓
ERROR
     ↓
rollback()
     ↓
exception continues
```

This is a very common backend pattern.

## Mental Model

```py
              with
               │
       ┌───────┴───────┐
       │               │
    __enter__       __exit__
       │               │
     setup           cleanup
       │               │
       └───────┬───────┘
               │
          YOUR CODE
```

And with `@contextmanager`:

```py
setup
  ↓
yield
  ↓
YOUR CODE
  ↓
resume
  ↓
cleanup
```
