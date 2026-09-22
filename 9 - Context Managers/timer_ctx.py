import time


class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        print(f"Execution time: {self.elapsed:.4f} seconds")


with Timer():
    total = sum(range(1_000_000))
    print(total)


with Timer() as timer:
    total = sum(range(1_000))

print(timer.elapsed)