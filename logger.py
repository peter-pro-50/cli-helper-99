import logging
from logging.handlers import RotatingFileHandler

class Logger:
    def __init__(self, name, level=logging.INFO, max_bytes=5*1024*1024, backup_count=2):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        handler = RotatingFileHandler(f'{name}.log', maxBytes=max_bytes, backupCount=backup_count)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def critical(self, message):
        self.logger.critical(message)

logger = Logger('cli_helper')
logger.log('Logger initialized.')