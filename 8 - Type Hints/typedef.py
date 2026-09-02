# Python doesn't enforce type hints at runtime — dict[str, int]
# is purely a hint/annotation for tools and humans, not something
# Python itself checks or blocks.
#
# So this line runs completely fine with zero warning or error from Python itself:
# users: dict[str, int] = {"John": 25, "Mike": 30, "Ross": "323i"}

numbers: list[int] = [1, 2, 3]

names: list[str] = ["John", "Mike", "Sarah"]

prices: list[float] = [10.5, 20.99]

users: dict[str, int] = {"John": 25, "Mike": 30}

# Nested Types
users_list: list[dict[str, str]] = [
    {"name": "John", "email": "john@test.com"},
    {"name": "Sarah", "email": "sarah@test.com"},
]

products: dict[str, list[int]] = {
	"laptops": [100, 200, 300],
	"phones": [400, 500]
}

user: tuple[str, int] = ("John", 30)
coordinates: tuple[float, float] = (28.61, 77.23)

# Variadic Tuple
numbers_tuple: tuple[int, ...] = (1, 2, 3, 4, 5)

# Returns either a string or None
def find_user(user_id: int) -> str | None:
		if user_id == 1:
				return "John"
		elif user_id == 2:
				return "Mike"
		else:
				return None

def greet(name: str, age: int | None = None):
	# Avoid using
  # if age: as "0" is falsy and will not be printed
	if age is not None:
		print(f"Hello {name}, you are {age} years old.")
	else:
		print(f"Hello {name}!")
