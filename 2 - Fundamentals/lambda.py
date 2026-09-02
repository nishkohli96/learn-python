# lambda creates small, anonymous (unnamed) functions in a
# single expression — no def, no name, no return keyword needed.
# Basic syntax -> lambda arguments: expression
#
# Rule of thumb: if it needs a name, multiple lines, or you're
# going to reuse it — write a real def function. Lambdas are
# for quick, inline, one-off logic, most often as an argument
# to another function.

square = lambda x: x ** 2
print(square(5))

add = lambda x, y: x + y
add(3, 4)  # 7

nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# sorted() / .sort() with a custom key:
# would thow err if I write sth else instead of "key"
people = [("Alice", 30), ("Bob", 25), ("Amy", 35)]
sorted(people, key=lambda person: person[1])
# A list of tuples. Each tuple is (name, age).
#
# Output -> [('Bob', 25), ('Alice', 30), ('Amy', 35)]
#
# The goal: sort this list of people by age, not by name.
# If you just did sorted(people), Python would sort tuples
# the default way — comparing the first element of each
# tuple first (i.e., alphabetically by name):
# sorted(people)
# [('Alice', 30), ('Amy', 35), ('Bob', 25)]  ← sorted by name, not what we want
#
# To sort by age instead, you need to tell sorted(): "for each item,
# here's the value to compare it by." That's what key= does.

# Bonus — sort descending (oldest first):
sorted(people, key=lambda person: person[1], reverse=True)
# [('Amy', 35), ('Alice', 30), ('Bob', 25)]