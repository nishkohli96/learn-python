# squares = []
# for i in range(5):
#     squares.append(i * i)

# Instead of this, use comprehensions -

squares = [i * i for i in range(5)]
print("squares upto 5", squares)

# Another example
evens = [i for i in range(10) if i % 2 == 0]
print(f"evens in range(1,10): {evens}")
print(type(evens))

# Dictionary comprehension
# prints - {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
squares_dict = {x: x * x for x in range(5)}
print(squares_dict)
print(type(squares_dict))

# Set comprehension
nums = {x * x for x in range(5)}
print(nums)
