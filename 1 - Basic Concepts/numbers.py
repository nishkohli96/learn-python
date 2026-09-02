import math

x = 3 + 4j
y = 5 + 2j
print(f"imaginary_num: {x + y}")

print(f"10 + 3 = {10 + 3}")
print(f"10 - 3 = {10 - 3}")
print(f"10 * 3 = {10 * 3}")
# Floating point result for division
print(f"10 / 3 = {10 / 3}")
# Integeral result for division
print(f"10 // 3 = {10 // 3}")
# Eq -> 10 * 10 * 10
print(f"10 ** 3 = {10**3}")

x = 20
x += 5
print(f"x += 5 = {x}")

print(f"round(2.9) = {round(2.9)}")
print(f"abs(-2.9) = {abs(2.9)}")


# For all functions imported from "math" module, refer
# https://docs.python.org/3/library/math.html

print(f"math.ceil(2.75) = {math.ceil(2.75)}")
print(f"math.factorial(10) = {math.factorial(10)}")

print(f"math.gcd(7, 70, 35) = {math.gcd(7, 70, 35)}")

# Returns the nearest integer, whose sq is <=n, where n
# must be an integer.
print(f"math.isqrt(55) = {math.isqrt(55)}")

# Evaluates to n! / (n - k)! when k <= n and evaluates to zero when k > n.
print(f"math.perm(6) = {math.perm(6)}")
print(f"math.perm(6, 2) = {math.perm(6, 2)}")

# Returns ASCII code
print("ord(B)", ord("B"))
print("ord(b)", ord("b"))

# Prints upto 3 decimal places. applying standard round-half-to-even
# rounding on that last digit. Since it's still a float, if the result
# happens to end in a trailing zero, Python won't show it.
# 
# (e.g. round(0.1005, 2) might print as 0.1 not 0.10).
print(round(10/34, 3)) # '0.294'

# 2. f-string formatting
#  This is usually what you want for display purposes, because
# it guarantees exactly 3 digits after the decimal point even
# if the last one is a zero:
x = 1
y = 4
print(f"{x/y:.5f}") # '0.25000' ← round() would just give you 0.25

print(format(22/7, '.4f'))
