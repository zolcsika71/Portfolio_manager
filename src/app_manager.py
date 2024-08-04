# app_manager.py

from logger.logging_config import LoggerConfig
import logging
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from gui.build import MainWindow, load_menu_structure
from src.db.create_db import DatabaseInitializer
import platform
from screeninfo import get_monitors  # Import screeninfo

# Setup logging
logger_config = LoggerConfig()
logger_config.setup_logging()
logger = logging.getLogger('app_manager')
monitor_number = 1


class ApplicationManager:
    def __init__(self, display_on=1):
        self.menu_structure = 'src/gui/structure.json'
        self.monitor_number = display_on  # Add monitor number
        self.app, self.main_window = self.run()

    @staticmethod
    def initialize_database():
        logger.info("Database module is running")
        DatabaseInitializer()

    def initialize_gui(self):
        logger.info("GUI build module is running")
        app = QApplication([])
        if platform.system() == 'Darwin':
            # Ensure the menu appears on macOS
            app.setAttribute(Qt.AA_DontUseNativeMenuBar)
        menu_structure = load_menu_structure(self.menu_structure)
        main_window = MainWindow(menu_structure)

        # Set the main window on the specified monitor
        self.set_window_on_monitor(main_window)

        main_window.show()
        return app, main_window

    def set_window_on_monitor(self, window):
        monitors = get_monitors()
        if monitor_number < len(monitors):
            monitor = monitors[self.monitor_number]
            window.setGeometry(monitor.x, monitor.y, window.width(), window.height())
        else:
            logger.warning(f"Monitor number {monitor_number} is out of range. Only {len(monitors)} monitors detected.")

    def run(self):
        logger.info("Application manager is running")
        self.initialize_database()
        app, main_window = self.initialize_gui()
        return app, main_window
