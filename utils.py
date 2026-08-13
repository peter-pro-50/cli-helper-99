import time
import requests

class RetryException(Exception):
    pass

def retry_request(url, max_attempts=5, backoff_factor=0.3):
    attempts = 0
    while attempts < max_attempts:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()  # Assuming the response is JSON
        except requests.exceptions.HTTPError as errh:
            print(f"Http Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Something went wrong: {err}")
        attempts += 1
        time.sleep(backoff_factor * (2 ** attempts))  # Exponential backoff
    raise RetryException(f"Failed to fetch {url} after {max_attempts} attempts")
