import time
from functools import wraps


def benchmark(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        print(f"{func.__name__} executed in {elapsed:.4f} seconds")
        return result
    return wrapper


@benchmark
def expensive_computation(n):
    total = 0
    for i in range(n):
        total += sum(j * j for j in range(1000))  # Simulates a heavy computation
    return total


@benchmark
def optimized_computation(n):
    return n * (999500000)  # Using the formula for sum of squares directly


if __name__ == "__main__":
    print(expensive_computation(5))
    print(optimized_computation(5))