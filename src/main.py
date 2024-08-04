# main.py

from app_manager import ApplicationManager
from logger.logging_config import LoggerConfig
import logging
import sys

# Setup logging
logger_config = LoggerConfig()
logger_config.setup_logging()
logger = logging.getLogger('main')


def main():
    logger.info("Application started")
    try:
        app = ApplicationManager()
        sys.exit(app.app.exec_())
    except RuntimeError as e:
        logger.error("Qt application error occurred", exc_info=True)
    except SystemExit as e:
        logger.info("System exit with code: %s", e.code)
    except Exception as e:
        logger.error("An unexpected error occurred", exc_info=True)
        raise  # Re-raise the exception after logging
    finally:
        logger.info("Application ended")


if __name__ == "__main__":
    main()
