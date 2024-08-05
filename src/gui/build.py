import json
import os
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QMenu, QMessageBox
from .styling import set_styling
import logging
from logger.logging_config import LoggerConfig
import importlib

# Setup logging
logger_config = LoggerConfig()
logger_config.setup_logging()
logger = logging.getLogger('build')


def convert_to_functions_name(name):
    """
    Convert spaces in the name to underscores.
    Convert capital letters to lowercase.
    """
    converted_name = name.replace(' ', '_').lower()
    return converted_name


def run_app_function(function_name):
    """
    Dynamically import and run a function from the app_functions directory.

    :param function_name: Name of the function to be imported and run.
    """
    module_path = '.app_functions.' + function_name
    try:
        logger.debug(f"Running function: {module_path}")
        module = importlib.import_module(module_path, package='app_functions')  # assuming 'src' is your package name
        func = getattr(module, function_name)
        func()
        logger.info(f"Action: {function_name} triggered.")
    except ModuleNotFoundError:
        logger.error(f"Module '{module_path}' not found.")
    except AttributeError:
        logger.error(f"Function '{function_name}' not found in module.")
    except Exception as e:
        logger.error(f"Error running '{function_name}': {str(e)}")


def load_menu_structure(file_path):
    """
    Load the menu structure from a JSON file.
    :param file_path: Path to the JSON file.
    :return: Dictionary containing the menu structure.
    """
    logger.info(f"Loading menu structure from {file_path}")
    if not os.path.isfile(file_path):
        logger.error(f"{file_path} does not exist or is not a file.")
        return None

    try:
        with open(file_path, 'r') as file:
            return json.load(file)["gui"]
    except (IOError, ValueError) as e:
        logger.error(f"Error reading {file_path}: {str(e)}")
        return None


# noinspection PyUnresolvedReferences
def create_menu_action(name):
    """
    Create a menu action with the given name.

    :param name: Name of the menu action.
    :return: A function to be called when the menu action is triggered.
    """

    def menu_action():
        # Convert spaces to underscores in the logger's name
        converted_name = convert_to_functions_name(name)
        logger.info(f"{name} triggered")
        logger.debug(f"{converted_name} will run")
        run_app_function(converted_name)

    return menu_action


class MainWindow(QMainWindow):
    def __init__(self, menu_structure, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.menu_structure = menu_structure
        self.init_ui()

    def init_ui(self):
        set_styling(self)
        menu_bar = self.menuBar()
        self.create_menus(menu_bar, self.menu_structure)
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Portfolio Manager')
        self.show()

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

        menu_bar.addSeparator()
        menu_bar.addAction("Exit", self.confirm_exit)

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
