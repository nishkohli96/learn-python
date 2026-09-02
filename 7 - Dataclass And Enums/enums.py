from enum import Enum


class OrderStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

status = OrderStatus.PENDING
print(status)
print(status.value)

for status in OrderStatus:
    print(f"Status: {status}")
    print(f"Value: {status.value}")