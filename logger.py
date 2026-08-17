import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name, log_file, level=logging.DEBUG):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=2)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

logger = setup_logger('cli_helper', 'cli_helper.log')
logger.info('Logger setup complete.')