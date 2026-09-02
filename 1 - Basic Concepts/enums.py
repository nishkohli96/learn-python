from enum import Enum


class Months(Enum):
    JAN = 1
    FEB = 2
    MAR = 3


val = Months.FEB

# Months.FEB
print(f"val: {val}")
if val == Months.FEB:
    print("yes")
