import time
import random

class RetryException(Exception):
    pass

def retry_network_operation(func, retries=3, delay=2):
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            if attempt < retries - 1:
                wait_time = delay * (2 ** attempt) + random.uniform(0, 1)
                print(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait_time:.2f} seconds...")
                time.sleep(wait_time)
            else:
                raise RetryException(f"All {retries} retries failed: {e}")

# Example network operation

def example_network_operation():
    if random.choice([True, False]):
        raise ConnectionError("Simulated network failure")
    return "Network operation succeeded!"

if __name__ == '__main__':
    try:
        result = retry_network_operation(example_network_operation)
        print(result)
    except RetryException as e:
        print(e)