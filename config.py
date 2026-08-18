import logging
import logging.handlers

# Logger configuration function

def setup_logger(log_file, log_level=logging.INFO):
    logger = logging.getLogger()
    logger.setLevel(log_level)

    # Create a rotating file handler
    handler = logging.handlers.RotatingFileHandler(
        log_file, maxBytes=5*1024*1024, backupCount=5
    )
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger

# Example of using the logger setup
if __name__ == '__main__':
    logger = setup_logger('app.log')
    logger.info('Logger is set up successfully!')
    logger.warning('This is a warning message.')
    logger.error('This is an error message.')
