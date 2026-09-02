def add_numbers(*a):
    return sum(a)


def subtract(a, b):
    return a - b


def multiply_nums(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b
