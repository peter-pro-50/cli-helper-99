import time

class Timer:
    def __init__(self):
        self.start = None

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        duration = time.time() - self.start
        print(f"Executed in: {duration:.4f} seconds")


def expensive_operation(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total


def main(n=1000000):
    with Timer():
        result = expensive_operation(n)
        print(f"Result: {result}")


if __name__ == '__main__':
    main()