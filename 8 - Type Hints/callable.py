# priort to py 3.9 it was imported from typing module, which is now deprecated.
# Callable is now imported from collections.abc module
from collections.abc import Callable


def execute(operation: Callable[[int], int], value: int) -> int:
    return operation(value)


def square(x: int) -> int:
    return x * x


result = execute(square, 5)

print(result)
