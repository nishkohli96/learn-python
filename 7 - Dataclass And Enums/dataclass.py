from dataclasses import dataclass, field


@dataclass
class User:
    name: str
    age: int


user = User("John", 30)

print(user)


@dataclass
class Product:
    name: str
    price: float
    quantity: int = 1  # default value

    def total_price(self):
        return self.price * self.quantity


product = Product(name="Laptop", price=75000, quantity=2)

print(product.total_price())

#field(default_factory=list) is how you give a mutable default
# value (like a list, dict, or set) to a dataclass field
# — something you actually can't do with a plain = [] default,
# because of a classic Python gotcha around mutable defaults.
#
# Instead of a single default value created once,
# default_factory takes a callable (a zero-argument function
#  that gets called fresh, once per new instance, to produce
# a brand-new list each time. list itself is just a callable
# that returns a new empty list when called (list() → []) — same idea as dict, set.
@dataclass
class UserWithSkills:
    name: str
    skills: list = field(default_factory=list)


user1 = UserWithSkills("Nishant")
user2 = UserWithSkills("Rahul")

user1.skills.append("Python")

print(user1.skills)  # ['Python']
print(user2.skills)  # []


# Sometimes you don't want the object to be modified after creation.
@dataclass(frozen=True)
class Point:
    x: int
    y: int

point = Point(10, 20)
# point.x = 30  # This will raise an error because the dataclass is frozen