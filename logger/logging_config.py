# /Users/zoltanka/Documents/Prog/Python/Portfolio_manager/logger/logging_config.py

import logging
import logging.config
import os
from colorlog import ColoredFormatter
from typing import Dict


class LoggerConfig:
    LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')

    def __init__(self) -> None:
        self.ensure_log_dir_exists()
        self.LOGGING_CONFIG = self.get_logging_config()

    @staticmethod
    def ensure_log_dir_exists() -> None:
        if not os.path.exists(LoggerConfig.LOG_DIR):
            os.makedirs(LoggerConfig.LOG_DIR)

    @staticmethod
    def get_file_handler(filename: str) -> Dict:
        return {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': filename,
            'mode': 'w',  # overwrite mode
            'formatter': 'standard',
        }

    def get_logging_config(self) -> Dict:
        return {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'standard': {
                    'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
                },
                'colored': {
                    '()': ColoredFormatter,
                    'format': '%(log_color)s%(asctime)s [%(levelname)s] %(name)s: %(message)s',
                    'log_colors': {
                        'DEBUG': 'cyan',
                        'INFO': 'green',
                        'WARNING': 'yellow',
                        'ERROR': 'red',
                        'CRITICAL': 'bold_red',
                    },
                },
            },
            'handlers': {
                'console': {
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',
                    'formatter': 'colored',
                },
                'file_combined': self.get_file_handler(os.path.join(self.LOG_DIR, 'portfolio_manager.log')),
            },
            'root': {
                'handlers': ['console', 'file_combined'],
                'level': 'DEBUG',
            }
        }

    def setup_logging(self) -> None:
        logging.config.dictConfig(self.LOGGING_CONFIG)

    @staticmethod
    def get_module_logger(module_name: str) -> logging.Logger:
        logger = logging.getLogger(module_name)
        file_handler = logging.FileHandler(os.path.join(LoggerConfig.LOG_DIR, f'{module_name}.log'))
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s'))
        logger.addHandler(file_handler)
        return logger


# Usage
if __name__ == "__main__":
    logger_config = LoggerConfig()
    logger_config.setup_logging()
    logger = LoggerConfig.get_module_logger('main')
    logger.info("Logging setup complete")
