import time
import random

def retry_operation(operation, retries=5, delay=2, backoff=2):
    """Attempts to execute a given operation, retrying on failure."""
    for attempt in range(retries):
        try:
            return operation()
        except Exception as e:
            if attempt < retries - 1:
                wait_time = delay * (backoff ** attempt)
                print(f'Attempt {attempt + 1} failed: {e}. Retrying in {wait_time:.1f} seconds...')
                time.sleep(wait_time)
            else:
                print(f'All {retries} attempts failed.')
                raise

# Example usage:
if __name__ == '__main__':
    def unstable_network_call():
        if random.random() < 0.7:
            raise ValueError('Network error!')
        return 'Success!'

    try:
        result = retry_operation(unstable_network_call)
        print(result)
    except Exception as e:
        print(f'Final error: {e}')
