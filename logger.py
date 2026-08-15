import logging

class Logger:
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def info(self, message: str):
        self.logger.info(message)

    def error(self, message: str):
        self.logger.error(message)

    def debug(self, message: str):
        self.logger.debug(message)

    def warning(self, message: str):
        self.logger.warning(message)

if __name__ == '__main__':
    logger = Logger('CLIHelper99')
    logger.info('Starting application...')

    while True:
        user_input = input('Enter a command: ')
        if not user_input.strip():
            logger.error('Empty input provided.')
            continue
        elif len(user_input) > 50:
            logger.error('Input exceeds maximum length of 50 characters.')
            continue
        logger.info(f'Processing input: {user_input}')  
        # Here, actual processing of input would occur
        if user_input.lower() == 'exit':
            logger.info('Exiting application...')
            break
        # Assume further processing occurs here