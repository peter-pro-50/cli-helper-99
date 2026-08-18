import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name, log_file, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=3)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

if __name__ == '__main__':
    log = setup_logger('example_logger', 'app.log')
    log.info('This is an info message')
    log.error('This is an error message')
    log.debug('This is a debug message')