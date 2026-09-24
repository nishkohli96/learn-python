from dataclasses import dataclass
from typing import Generic, TypedDict, TypeVar

T = TypeVar("T")


class User(TypedDict):
    id: int
    name: str
    email: str

class Product(TypedDict):
    id: int
    name: str
    price: float
    inventory_count: int


class Repository(Generic[T]):
    def __init__(self):
        self.items: list[T] = []

    def add(self, item: T) -> None:
        self.items.append(item)

    def get_all(self) -> list[T]:
        return self.items

user: User = {"id": 1, "name": "John", "email": "john@example.com"}
product: Product = {"id": 1, "name": "Laptop", "price": 999.99, "inventory_count": 10}

user_repository = Repository[User]()
product_repository = Repository[Product]()

@dataclass
class Response(Generic[T]):
    data: T # or list[T]
    success: bool

user_response = Response(
    data=user,
    success=True
)
product_response = Response(product,True)

print(user_response.data)
