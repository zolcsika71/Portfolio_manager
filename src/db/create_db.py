# db/create_db.py

import os
import sqlite3
import logging
from logger.logging_config import setup_logging
from src.db.table_definitions import SQL_QUERIES  # Import the SQL_QUERIES

setup_logging()
logger = logging.getLogger('db')


class DatabaseManager:
    """Class to manage database creation and connection."""

    def __init__(self):
        """Initialize the DatabaseManager with paths and existence check."""
        self.project_dir = os.path.dirname(os.path.abspath(os.path.join(__file__, "..", "..", "main.py")))
        self.db_folder = os.path.join(self.project_dir, "db")
        self.db_path = os.path.join(self.db_folder, "investments.db")
        self.db_exists = os.path.exists(self.db_path)
        self.check_db_exists()

    def check_db_exists(self):
        """Check if the database exists, if not create it."""
        if not self.db_exists:
            self.create_database()
        else:
            logger.info("Database already exists")

    def create_database(self):
        """Create the database and log the process."""
        logger.info("Database not exists")
        logger.info("Creating database")
        try:
            self._create_database()
            logger.info("Database created successfully")
            return True
        except sqlite3.Error as e:
            logger.error(f"Error creating database: {e}", exc_info=True)
            return False

    def _create_database(self):
        """Connect to the SQLite database and create tables."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        self._create_tables(cursor)

    @staticmethod
    def _create_tables(cursor):
        """Execute the table creation queries."""
        for query in SQL_QUERIES:
            cursor.execute(query)
        cursor.connection.commit()


if __name__ == "__main__":
    DatabaseManager()
