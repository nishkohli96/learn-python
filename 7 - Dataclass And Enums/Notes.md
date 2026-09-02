# Dataclasses & Enums

## Dataclasses

Python provides a convenient way to create classes that primarily hold data.

```py
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

To reduce above boilerplate, Python provides:

```py
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

user = User("John", 30)
```

**A Python dataclass is an actual class and can have methods, behavior, etc.**

The dataclass automatically generates useful methods such as:

```py
__init__
__repr__
__eq__
```

**When you don't want the object to be modified after creation.**
```py
@dataclass(frozen=True)
```

## Enums

```py
from enum import Enum


class OrderStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

status = OrderStatus.PENDING
```

### Comparison

```py
if status == OrderStatus.PENDING:
    print("Order hasn't started")

status.value == "pending"
```
