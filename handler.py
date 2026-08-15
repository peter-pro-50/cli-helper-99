import time
import random
import requests

class NetworkError(Exception):
    pass

class NetworkHandler:
    def __init__(self, retries=3, delay=2):
        self.retries = retries
        self.delay = delay

    def make_request(self, url):
        for attempt in range(self.retries):
            try:
                response = requests.get(url)
                response.raise_for_status()
                return response.json()
            except requests.RequestException as e:
                if attempt < self.retries - 1:
                    time.sleep(self.delay * (2 ** attempt))  # Exponential backoff
                else:
                    raise NetworkError(f"Failed to retrieve data after {self.retries} attempts: {e}")

if __name__ == '__main__':
    handler = NetworkHandler(retries=5, delay=1)
    try:
        data = handler.make_request('https://api.example.com/data')
        print(data)
    except NetworkError as ne:
        print(ne)