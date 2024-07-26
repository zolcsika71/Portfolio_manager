import logging
import logging.config
import os
from colorlog import ColoredFormatter

LOG_DIR = os.path.join(os.path.dirname(__file__), 'logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)


# Function to create a file handler that overwrites the log file each run
def get_file_handler(filename):
    return {
        'level': 'DEBUG',
        'class': 'logging.FileHandler',
        'filename': filename,
        'mode': 'w',  # overwrite mode
        'formatter': 'standard',
    }


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
        'file_db': get_file_handler(os.path.join(LOG_DIR, 'db.log')),
        'file_gui_build': get_file_handler(os.path.join(LOG_DIR, 'gui_build.log')),
        'file_gui_get_structure': get_file_handler(os.path.join(LOG_DIR, 'gui_get_structure.log')),
        'file_combined': get_file_handler(os.path.join(os.path.dirname(__file__), 'Portfolio_manager.log')),
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
        'gui.build': {
            'handlers': ['file_gui_build'],
            'level': 'DEBUG',
            'propagate': False
        },
        'gui.get_structure': {
            'handlers': ['file_gui_get_structure'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}


def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)
