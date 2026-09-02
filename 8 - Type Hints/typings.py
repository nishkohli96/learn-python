from typing import Literal, NotRequired, Protocol, TypedDict, TypeVar

T = TypeVar("T")


def first(items: list[T]) -> T:
    return items[0]


print(first([1, 2, 3]))
print(first(["a", "b", "c"]))

# TypedDict doesn't create a runtime class/object like a dataclass does.
# It's primarily for static type checking.
class User(TypedDict):
    id: int
    name: str
    email: str


user: User = {"id": 1, "name": "John", "email": "john@test.com"}


class Speaker(Protocol):
    def speak(
        self,
    ) -> str: ...  # just the signature - no implementation, this is a contract


def make_sound(animal: Speaker):
    return animal.speak()


class Dog:
    def speak(self):
        return "Woof"


class Cat:
    def speak(self):
        return "Meow"


make_sound(Dog())
make_sound(Cat())

# Literals
# Prefer using Enum, when you need actual runtime values/behavior.
def update_status(
    status: Literal["pending", "completed", "cancelled"]
):
    print(f"Status updated to: {status}")

update_status("pending")      # ✅
update_status("completed")    # ✅
# update_status("random")       # ❌ type checker

class UserDetails(TypedDict):
    id: int
    name: str
    roles: list[str]
    age: NotRequired[int]
