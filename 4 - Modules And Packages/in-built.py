# Python comes with a huge standard library.
import math
import os
import random
from datetime import datetime, timezone

print(math.sqrt(25))  # 5.0

number = random.randint(1, 10)
# Return random integer in range [a, b], both inclusive.
print(number)

# /Users/nish/coding/python/learn
print(os.getcwd())

# It is recommended to always use timezone-aware objects
# If tz not provided, it uses local time
#
# 2026-08-13 11:48:30.411718+00:00
now = datetime.now(tz=timezone.utc)
print(now)
