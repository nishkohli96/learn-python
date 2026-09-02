# Python doesn't enforce types, but hints improve
# readability and editor support.

# This tells readers (and tools like VS Code):
# - a should be an int
# - b should be an int
# - the function returns an int

# Docstrings are like jsdocs for functions,
# but are defined after function def, not before
def add(a: int, b: int = 2) -> int:
    """Return the sum of two integers."""
    return a + b


print(add(3, 5))

