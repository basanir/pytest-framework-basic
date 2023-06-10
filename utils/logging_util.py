import logging
import os
from datetime import datetime

class Logger:

    def __init__(self, name, log_dir='logs', level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.log_file = self._get_log_file(name)

        # remove handlers so that we don't get duplicate messages in the log file
        # Also, this will allow us to set the log level for each test
        while self.logger.handlers:
            self.logger.handlers.pop()

        # create log directory if it doesn't exist
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # create handlers
        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(self.log_file)

        # set log level
        console_handler.setLevel(level)
        file_handler.setLevel(level)

        # create a logging format
        formatter = logging.Formatter('[%(asctime)s] [%(name)-20s::%(funcName)-25s] [%(levelname)-8s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # add the handlers to the logger
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    def get_logger(self):
        # return the logger
        return self.logger
    
    @staticmethod
    def _get_log_file(name):
        # create log file name with date and time and remove .py extension
        date = datetime.now().strftime("%Y%m%d_%H%M%S")
        name = name.replace(".py", "")
        return os.path.join("logs", f"{name}_{date}.log")


