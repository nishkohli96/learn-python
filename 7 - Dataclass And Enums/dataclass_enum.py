from dataclasses import dataclass
from enum import Enum


class OrderStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


@dataclass
class Order:
    id: int
    customer: str
    amount: float
    status: OrderStatus

# You automatically get useful behavior such as an initializer
# and readable representation.
order = Order(
  id=101,
  customer="Devon",
  amount=5000,
  status=OrderStatus.PENDING
)

# prints - Order(id=101, customer='Devon', amount=5000, status=OrderStatus.PENDING)
# Without needing to manually write __init__.
print(order)
