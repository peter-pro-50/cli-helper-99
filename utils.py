import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

@measure_time
def optimized_function(data):
    result = []
    unique_data = set(data)
    for item in unique_data:
        if item % 2 == 0:
            result.append(item ** 2)
    return result

if __name__ == '__main__':
    sample_data = range(1000000)
    print(optimized_function(sample_data))