MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30
RETRY_ATTEMPTS = 5
ERROR_MESSAGES = {
    'connection_failed': 'Unable to connect, please try again.',
    'timeout': 'The operation timed out.',
    'invalid_input': 'The input provided is invalid.',
    'not_found': 'The requested resource was not found.'
}

STATUS_CODES = {
    200: 'OK',
    400: 'Bad Request',
    404: 'Not Found',
    500: 'Internal Server Error'
}

API_ENDPOINTS = {
    'user': '/api/v1/user',
    'post': '/api/v1/post',
    'comment': '/api/v1/comment'
}

CACHE_EXPIRY = 600  # seconds
MAX_RETRIES = 3
