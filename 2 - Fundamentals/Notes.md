# Fundamentals

`__pycache__` = auto-gen folder, hold compiled bytecode (`.pyc` file) for each module. Python creates it on runtime to speed up next import (skip re-compile source if unchanged).

Safe to delete anytime, auto regenerates. Usually `.gitignore` it.

## Functions

When Python looks for a variable, it searches in this order:

```
Local -> Enclosing -> Global -> Built-in
```

Example:

```py
name = "Global"

def outer():
    name = "Outer"

    def inner():
        name = "Inner"
        print(name)

    inner()

outer() # Output -> "Inner"
```

**Python finds the closest matching variable first.**

## Exceptions

`try` must have at least one `except` or `finally` clause.

```py
try:
    print("Try")
except:
    print("Except")
else:
    print("Else")
finally:
    print("Finally")
```

Remember:
- **try** → code that may fail
- **except** → runs if an exception occurs
- **else** → runs only when no exception occurs
- **finally** → always runs

### Common Built-in Exceptions

| Exception                             | When it occurs                                 |
| ------------------------------------- | ---------------------------------------------- |
| `ValueError`                          | Correct type, invalid value (`int("abc")`)     |
| `TypeError`                           | Wrong type (`5 + "hello"`)                     |
| `IndexError`                          | Invalid list index                             |
| `KeyError`                            | Missing dictionary key, (using [], not .get()) |
| `ZeroDivisionError`                   | Division by zero                               |
| `AttributeError`                      | Missing object attribute                       |
| `FileNotFoundError`                   | File doesn't exist                             |
| `ImportError` / `ModuleNotFoundError` | Import fails                                   |

#### Diff KeyError & AttributeError
| KeyError | AttributeError |
|-|-|
| Triggered by | dict["missing_key"] | obj.missing_attribute |
| Data type involved | dicts (and dict-like mappings) | any object — instances, strings, modules, etc.|
| Common cause | typo in key name, or key genuinely absent | typo in attribute name, calling wrong method, or None sneaking in where an object was expected |
| Safe alternative | dict.get("key", default) | getattr(obj, "attr", default) or hasattr(obj, "attr") |

## Decorator

```
Decorator
    ↓
takes a function
    ↓
creates wrapper
    ↓
adds behavior
    ↓
returns wrapper
```

**Syntax**
```py
def decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        # before
        result = func(*args, **kwargs)
        # after
        return result

    return wrapper
```

Decorator with value:

```py
def decorator_config(value):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            # use value
            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator
```

```py
@repeat(3)
def hello():
    print("Hello")
```
Executes this function 3 times.
