import json
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QMenu, QMessageBox
from .styling import set_styling
import logging
from logger.logging_config import LoggerConfig


# Setup logging
logger_config = LoggerConfig()
logger_config.setup_logging()
logger = logging.getLogger('build')


def load_menu_structure(file_path):
    """
    Load the menu structure from a JSON file.

    :param file_path: Path to the JSON file.
    :return: Dictionary containing the menu structure.
    """
    logger.info(f"Loading menu structure from {file_path}")
    with open(file_path, 'r') as file:
        return json.load(file)["gui"]


# noinspection PyUnresolvedReferences
def create_menu_action(name):
    """
    Create a menu action with the given name.

    :param name: Name of the menu action.
    :return: A function is to be called when the menu action is triggered.
    """

    def menu_action():
        logger.debug(f"{name} selected")

    return menu_action


# noinspection PyUnresolvedReferences
class MainWindow(QMainWindow):
    """
    Main window class for the application.
    """

    def __init__(self, menu_structure):
        """
        Initialize the main window.

        :param menu_structure: Dictionary containing the menu structure.
        """
        super().__init__()
        self.setWindowTitle('Portfolio Manager')
        self.setGeometry(100, 100, 1024, 768)
        set_styling(self)
        menu_bar = self.menuBar()
        self.create_menus(menu_bar, menu_structure)
        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.confirm_exit)
        menu_bar.addAction(exit_action)

    def create_menus(self, menu_bar, menu_structure):
        """
        Create menus dynamically from the given structure.

        :param menu_bar: The main menu.
        :param menu_structure: Dictionary containing the menu structure.
        """
        logger.info("Creating menus")
        for main_menu in menu_structure["main_menu_items"]:
            if main_menu["available"]:
                if main_menu["sub_menu_items"]:
                    menu = menu_bar.addMenu(main_menu["name"])
                    self.add_sub_menus(menu, main_menu["sub_menu_items"])
                else:
                    action = QAction(main_menu["name"], self)
                    action.triggered.connect(create_menu_action(main_menu["name"]))
                    menu_bar.addAction(action)

    def add_sub_menus(self, parent_menu, sub_menu_items):
        """
        Add submenus to a parent menu.

        :param parent_menu: The parent menu to which submenus will be added.
        :param sub_menu_items: List of submenu items.
        """
        logger.info("Adding sub-menus")
        for sub_menu in sub_menu_items:
            if sub_menu["available"]:
                if "sub_menu_items" in sub_menu and sub_menu["sub_menu_items"]:
                    menu = QMenu(sub_menu["name"], self)
                    parent_menu.addMenu(menu)
                    self.add_sub_menus(menu, sub_menu["sub_menu_items"])
                else:
                    action = QAction(sub_menu["name"], self)
                    action.triggered.connect(create_menu_action(sub_menu["name"]))
                    parent_menu.addAction(action)

    def confirm_exit(self):
        """
        Confirm exit action.
        """
        logger.info("Confirming exit")
        reply = QMessageBox.question(self, 'Confirmation',
                                     "Are you sure you want to exit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            qApp.quit()
