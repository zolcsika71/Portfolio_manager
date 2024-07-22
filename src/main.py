# main.py
import json
from db.create_db import DatabaseManager
from gui.app import PortfolioManagerApp


def main():
    # Create the database
    db_manager = DatabaseManager()

    # Load menu structure from JSON file
    with open('src/gui/structure.json', 'r') as file:
        menu_structure = json.load(file)

    # Initialize and run the GUI
    app = PortfolioManagerApp(menu_structure)
    app.run()


if __name__ == "__main__":
    main()

