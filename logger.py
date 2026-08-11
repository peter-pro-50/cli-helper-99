import logging
import logging.handlers

class LoggerSetup:
    def __init__(self, name, log_file, level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=5)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger

if __name__ == '__main__':
    log_setup = LoggerSetup('MyLogger', 'app.log')
    logger = log_setup.get_logger()
    logger.info('Logger initialized successfully.')
    logger.error('This is an error message.')
