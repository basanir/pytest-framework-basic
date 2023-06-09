import logging
import os

class Logger:

    def __init__(self, name, log_dir='logs', level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # create handlers
        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(f'{log_dir}/{name}.log')
        console_handler.setLevel(level)
        file_handler.setLevel(level)

        # create a logging format
        formatter = logging.Formatter('[%(asctime)s] [%(name)s] %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # add the handlers to the logger
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger

