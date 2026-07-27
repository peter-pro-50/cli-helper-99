import time
import requests

# Exponential backoff intervals in seconds
RETRY_INTERVALS = [1, 2, 4, 8, 16]

def retry_request(url, max_retries=5):
    attempt = 0
    while attempt < max_retries:
        try:
            response = requests.get(url)
            # Check for HTTP errors
            response.raise_for_status()
            return response.json()
        except (requests.HTTPError, requests.ConnectionError) as e:
            print(f'Attempt {attempt + 1} failed: {e}')
            if attempt < len(RETRY_INTERVALS):
                time.sleep(RETRY_INTERVALS[attempt])
            attempt += 1
    raise Exception(f'Request to {url} failed after {max_retries} attempts')
