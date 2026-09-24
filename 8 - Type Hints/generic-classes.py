from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get(self) -> T:
        return self.value


number_box = Box(100)
string_box = Box("hello")


# Generic API Response
@dataclass
class APIResponse(Generic[T]):
    data: T
    status_code: int
    message: str
