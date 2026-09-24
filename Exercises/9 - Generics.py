from dataclasses import dataclass
from typing import Generic, TypedDict, TypeVar

# 1. Generic function reverse_pair to reverse the order of two elements
X = TypeVar("X")
Y = TypeVar("Y")


def reverse_pair(a: X, b: Y) -> tuple[Y, X]:
    return (b, a)


print(reverse_pair(10, "John"))


# 2. Generic function get_list_length to return the length of a list
def get_list_length(arr: list) -> int:
    return len(arr)


print(get_list_length([1, 2, 3, 4, 5]))

# 3. Constrained TypeVar to accept int or float and return the double of the value
Z = TypeVar("Z", int, float)


def double(value: Z) -> Z:
    return value * 2


print(double(5))
print(double(3.14))


# 4. Bounded TypeVar to accept only subclasses of Animal
class Animal:
    def speak(self) -> str:
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
    def speak(self) -> str:
        return "Woof"


class Cat(Animal):
    def speak(self) -> str:
        return "Meow"


AnmG = TypeVar("AnmG", bound=Animal)


def get_animal(animal: AnmG) -> AnmG:
    return animal


dg = get_animal(Dog())
print(dg.speak())


# 5. Generic class with get() method to return the content of the box
@dataclass
class Box(Generic[X]):
    content: X

    def get(self) -> X:
        return self.content


box_num = Box(100)
print(box_num.get())

box_str = Box("hello")
print(box_str.get())


# 6. Generic API Response class to hold data, status code, and message
@dataclass
class APIResponse(Generic[X]):
    data: X
    success: bool
    message: str


class User(TypedDict):
    id: int
    name: str
    email: str


class Product(TypedDict):
    id: int
    name: str
    price: float
    inventory_count: int


user: User = {"id": 1, "name": "John", "email": "test@yopmail.com"}

user_response = APIResponse(data=user, success=True, message="User found")
