import logging
import os

class AppConfig:
    def __init__(self, config_file):
        self.config_file = config_file
        self.settings = self.load_settings()

    def load_settings(self):
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f'Config file {self.config_file} not found.')
        with open(self.config_file) as f:
            return f.read()

class AppLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

def run_application(config_path):
    config = AppConfig(config_path)
    app_logger = AppLogger('cli_helper')
    app_logger.logger.info('Starting application with config: {}'.format(config.settings))

if __name__ == '__main__':
    run_application('config.json')