import math

from calculator import add_nums, divide, multiply_nums, subtract

print(add_nums(2, 4))
print(add_nums(24, 48, 1, 12))

print(subtract(20, 8))
print(subtract(12, 15))

print(multiply_nums(12, 4))
print(multiply_nums(5, 7, 8))
math.prod([2, 4, 6])  # 48
math.prod([12, 5])  # 48

try:
    print(divide(15, 10))
except ValueError as v:
    print(v)
