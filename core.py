import time

class PerformanceTracker:
    def __init__(self):
        self.execution_times = []

    def track_time(self, func):
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            self.execution_times.append(end_time - start_time)
            return result
        return wrapper

    def average_time(self):
        return sum(self.execution_times) / len(self.execution_times) if self.execution_times else 0

performance_tracker = PerformanceTracker()

@performance_tracker.track_time
def sample_heavy_computation(n):
    total = 0
    for i in range(n):
        total += (i ** 2) * (i ** 0.5)
    return total

if __name__ == '__main__':
    for _ in range(10):
        print(sample_heavy_computation(10000))
    print("Average Execution Time:", performance_tracker.average_time())