from dataclasses import dataclass, field
from enum import Enum


@dataclass
class Book:
    title: str
    author: str
    price: float

    def discounted_price(self, percentage):
        return self.price * (1 - percentage / 100)


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 15)

print(book1)
print(book2)
print(book1.discounted_price(10))


@dataclass
class User:
    name: str
    age: int
    skills: list[str] = field(default_factory=list)


user1 = User("Alice", 30, ["Python", "JavaScript"])
user2 = User("Bob", 25)

print(user1)
print(user2)


class PaymentStatus(Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"
    REFUNDED = "refunded"


@dataclass
class Payment:
    id: int
    amount: float
    status: PaymentStatus = PaymentStatus.PENDING


payment1 = Payment(1, 100.0, PaymentStatus.PENDING)
print(payment1)
