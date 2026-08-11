import time
import random

class RetryConfig:
    def __init__(self, max_attempts=5, backoff_factor=1, jitter=False):
        self.max_attempts = max_attempts
        self.backoff_factor = backoff_factor
        self.jitter = jitter

    def backoff_time(self, attempt):
        backoff = self.backoff_factor * (2 ** attempt)
        if self.jitter:
            backoff += random.uniform(0, self.backoff_factor)
        return backoff

RETRY_CONFIG = RetryConfig()