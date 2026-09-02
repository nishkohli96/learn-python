from collections.abc import Callable
from typing import NotRequired, Protocol, TypedDict, TypeVar

# 1. Generic function to print last element
T = TypeVar("T")


def get_last(items: list[T]) -> T:
    return items[-1]


print(get_last([1, 2, 3]))
print(get_last(["ram", "shyam", "mohan", "geeta"]))


# 2. Function with Optional args
#   user_id → int
#   return → str OR None
def find_username(user_id: int) -> str | None:
    if user_id is None:
        return None
    return f"user_{user_id}"


print(find_username(123))


# 3. Function with Callable args
def apply_function(func: Callable[[int, int], int], val1: int, val2: int) -> int:
    return func(val1, val2)


def add(x: int, y: int) -> int:
    return x + y


print(apply_function(add, 5, 10))
print(apply_function(lambda x, y: x - y, 5, 10))


# 4. TypedDict
class Product(TypedDict):
    id: int
    name: str
    price: float
    in_stock: bool


p1: Product = {"id": 1, "name": "Laptop", "price": 999.99, "in_stock": True}


# 5. Protocol
class Printable(Protocol):
    def print_info(
        self,
    ) -> str: ...  # just the signature - no implementation, this is a contract


def print_stuff(printable: Printable) -> str:
    return printable.print_info()


class User:
    def print_info(self) -> str:
        return "User info: John Doe"


class ProductName:
    def print_info(self) -> str:
        return "Product name: Laptop"

print(print_stuff(User()))
print(print_stuff(ProductName()))
# 6. TypeScript → Python
# type User = {
#     id: number
#     name: string
#     roles: string[]
#     age?: number
# }


class UserDetails(TypedDict):
    id: int
    name: str
    roles: list[str]
    age: NotRequired[int]

user1: UserDetails = {
    "id": 1,
    "name": "John",
    "roles": ["admin"]
}