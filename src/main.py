# main.py


from db.create_db import DatabaseManager


def main():
    # Initialize the database
    db_manager = DatabaseManager()
    # Use the db_manager instance to suppress the unused variable warning
    _ = db_manager


if __name__ == "__main__":
    main()
