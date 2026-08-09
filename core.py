import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=3, backoff_factor=1):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Assuming the response is JSON
        except RequestException as e:
            retries += 1
            wait = backoff_factor * (2 ** (retries - 1))
            print(f'Request failed: {e}. Retrying in {wait} seconds...')
            time.sleep(wait)
    raise ConnectionError(f'Failed to retrieve data after {max_retries} attempts.')

# Example usage:
if __name__ == '__main__':
    try:
        data = retry_request('https://api.example.com/data')
        print('Data retrieved:', data)
    except ConnectionError as e:
        print(e)