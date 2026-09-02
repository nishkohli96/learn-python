class CountUp:
    def __init__(self, limit):
        self.current = 1
        self.limit = limit

    # Why __iter__ returning self matters ??
    # This is what makes CountUp a proper iterator. It means iter(counter)
    # returns the object itself, which is exactly why this also works
    # without any manual next() calls at all.
    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

    def reset(self):
        self.current = 1

    def printCurrentValue(self):
        print(f"Current value: {self.current}")


counter = CountUp(3)

try:
    while True:
        print(next(counter))
except StopIteration:
    print("End of iteration")

print("Resetting the counter...")
counter.reset()

# Print again using for loop, if both for-loop and
# even a single next(counter) runs, it throws
# StopIteration exception

# for num in counter:
#     print(num)
print(next(counter))
counter.printCurrentValue()
print(next(counter))
