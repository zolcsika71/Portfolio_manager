# app_manager.py

from logger.logging_config import LoggerConfig
import logging
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from gui.build import MainWindow, load_menu_structure
from src.db.create_db import DatabaseInitializer
import platform

# Setup logging
logger_config = LoggerConfig()
logger_config.setup_logging()
logger = logging.getLogger('app_manager')


class ApplicationManager:
    def __init__(self):
        self.menu_structure = 'src/gui/structure.json'
        self.app, self.main_window = self.run()

    def initialize_database(self):
        logger.info("Database module is running")
        DatabaseInitializer()

    def initialize_gui(self):
        logger.info("GUI build module is running")
        app = QApplication([])
        if platform.system() == 'Darwin':
            # Ensure the menu bar appears on macOS
            app.setAttribute(Qt.AA_DontUseNativeMenuBar)
        menu_structure = load_menu_structure(self.menu_structure)
        main_window = MainWindow(menu_structure)
        main_window.show()
        return app, main_window

    def run(self):
        logger.info("Application manager is running")
        self.initialize_database()
        app, main_window = self.initialize_gui()
        return app, main_window
