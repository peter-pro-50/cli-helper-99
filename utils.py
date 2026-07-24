import time
import requests
from functools import wraps

def retry(max_attempts=3, delay=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except requests.exceptions.RequestException as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")
                    if attempts < max_attempts:
                        time.sleep(delay)
                    else:
                        print("Max attempts reached. Raising exception.")
                        raise
        return wrapper
    return decorator

@retry(max_attempts=5, delay=1)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
