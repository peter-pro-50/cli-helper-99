import time
import random
import requests

class NetworkError(Exception):
    pass

class Retry:
    def __init__(self, retries=3, backoff=2, error_cls=NetworkError):
        self.retries = retries
        self.backoff = backoff
        self.error_cls = error_cls

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(self.retries):
                try:
                    return func(*args, **kwargs)
                except self.error_cls as e:
                    last_exception = e
                    sleep_time = self.backoff ** attempt
                    time.sleep(sleep_time)
                    print(f'Retry {attempt + 1}/{self.retries} after {sleep_time} seconds')
            raise last_exception
        return wrapper

@Retry(retries=5)
def fetch_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise NetworkError(f'Failed to fetch data from {url}')
    return response.json()