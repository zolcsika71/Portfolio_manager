# Portfolio_manager/src/main.py

import logging
from logger.logging_config import setup_logging
from src.db.create_db import DatabaseManager
from src.gui.build import MainWindow

setup_logging()
logger = logging.getLogger('main')


def main():
    logger.info("Application started")
    try:
        logger.info("Database module is running")
        DatabaseManager()
        logger.info("GUI build module is running")
        MainWindow()

    except Exception as e:
        logger.error("An error occurred", exc_info=True)  # Corrected line
    finally:
        logger.info("Application ended")


if __name__ == "__main__":
    main()