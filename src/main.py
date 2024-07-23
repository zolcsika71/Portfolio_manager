# Portfolio_manager/src/main.py

import logging
from logger.logging_config import setup_logging
from src.db.create_db import DatabaseManager

setup_logging()
logger = logging.getLogger('main')


def main():
    logger.info("Application started")
    try:
        DatabaseManager()
        logger.info("Application running")
    except Exception as e:
        logger.error("An error occurred", e, exc_info=True)
    finally:
        logger.info("Application ended")


if __name__ == "__main__":
    main()
