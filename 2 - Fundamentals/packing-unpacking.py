# Packing means Python collects values.

def test(*args):
    print(args)


test(1,2,3,4)
# Python packs them into -> (1,2,3,4)

# Unpacking
point = (10,20)
# Instead of
# x = point[0]
# y = point[1]
x, y = point
print("x: ", x)
print("y:", y)

# For Lists
a, b, c = [1,2,3]
print(a)

c = 10
d = 20

# Swapping variables
c, d = d, c
print("c:", c)
print("d:", d)

# Ignore values
x, _, z = [100,200,300]
print("x:", x)
print("y:", y)

# Collect remaining
first, *middle, last = [1,2,3,4,5]
print(first)  # 1
print(middle) # [2,3,4]
print(last)   # 5

fruits = ["apple", "tomato", "banana", "orange"]
f1, f2, *other_fruits = fruits
print(f1)
print(f2)
print(other_fruits)

nums = [2,3]
# Instead of print(sum([nums[0], nums[1]]))
print(sum([*nums]))