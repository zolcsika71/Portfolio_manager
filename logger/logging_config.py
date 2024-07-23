import logging
import logging.config
import os
from colorlog import ColoredFormatter

LOG_DIR = os.path.join(os.path.dirname(__file__), 'logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOGGING_CONFIG = {
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
        'file_db': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'db.log'),
            'formatter': 'standard',
        },
        'file_combined': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(os.path.dirname(__file__), 'Portfolio_manager.log'),
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file_combined'],
            'level': 'DEBUG',
            'propagate': True
        },
        'db': {
            'handlers': ['file_db'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}


def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)
