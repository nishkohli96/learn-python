# 1. Create an iterator and manually retrieve each value using next().
numbers = [10, 20, 30]
num_iter = iter(numbers)

for value in num_iter:
    print(value)


# 2. Custom iterator -> CountDown(5)
class CountDown:
    def __init__(self, counter):
        self.counter = counter

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < 0:
            raise StopIteration
        value = self.counter
        self.counter -= 1
        return value


count_iter = CountDown(5)
print(next(count_iter))
print(next(count_iter))
print("-----")

# 3. Write count_up(10) using generator
def count_till(limit: int):
    yield from range(1, limit + 1)


count_up_10 = count_till(10)

while True:
    try:
        print(next(count_up_10))
    except StopIteration:
        break
print("-----")


# 4. Create a generator that produces squares from 1 to 20.
def squares_till(limit: int):
    for x in range(1, limit + 1):
        yield x**2


squares_20 = squares_till(20)
for square in squares_20:
    print(square)
print("-----")

# 5. Even numbers: Create a generator that produces even numbers from 1 to 100.
gen_even = (x for x in range(1, 101) if x % 2 == 0)


# 6. Generator expression: Create a generator expression that produces:
# 1, 4, 9, 16, ..., 100


def squares_string(limit: int):
    result = ""
    for x in range(1, limit + 1):
        num_sq = x**2
        if x == 1:
            result = num_sq
            yield result
        else:
            result = f"{result}, {num_sq}"
            yield result


gen_squares = (x ** 2 for x in range(1, 11))
gen_squares_10 = squares_string(10)
while True:
    try:
        print(next(gen_squares_10))
    except StopIteration:
        break
print("-----")


# iterable: sth than can be iterated on. Eg list, dictionary
# iterator: the variable iterating over a list
# generator: pointer that iterates when next fn is called

# 7. for a large file generate a function, which yields only
# lines containing "ERROR" without loading the entire file into memory.
# def read_large_file(filepath):
#     with open(filepath) as f:
#         for line in f:
#            if "ERROR" in line:
#               yield line.strip()

# # Process a 10GB log file without ever holding it all in RAM
# for line in read_large_file("huge_server.log"):
#    print(line)
