
# Input from user, value will always be a string.
# Conversion of data types can be done using the following functions:
# - int(x)
# - float(x)
# - bool(x)
# - str(x)
#
# int(x) parse string direct, no decimal point allowed.
# "10.23" not valid int literal, ValueError throw.
# fix: go through float first, then int.
# Eg: z = int(float(x))

x = input("x: ")
print("typeof x ", type(x))
z = int(x)
y = z + 10
print(f"y: {y}")

# if a = 10, then c would be 30.0 
a = input("a: ")
b = float(a)
c = b + 20
print(f"c: {c}")
