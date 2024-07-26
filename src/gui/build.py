import sys
import logging
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QPushButton
from .get_structure import GuiStructureLoader
from .styling import set_styling

logger = logging.getLogger('gui_build')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        logger.info("Initializing the main window.")
        structure = GuiStructureLoader('gui/structure.json')
        gui_structure = structure['gui']

        self.setWindowTitle(structure['title'])
        logger.debug(f"Window title set to {structure['title']}")

        menu_bar = self.menuBar()
        for menu_item in gui_structure['main_menu_items']:
            self.create_menu(menu_bar, menu_item)

        set_styling(self)
        logger.info("Main window initialized successfully.")

    # noinspection PyUnresolvedReferences
    def create_menu(self, root, menu_item):
        menu = root.addMenu(menu_item["name"])
        logger.debug(f"Creating menu: {menu_item['name']}")
        if menu_item.get("sub_menu_items"):
            for sub_item in menu_item["sub_menu_items"]:
                self.create_menu(menu, sub_item)
        else:
            action = QAction(menu_item["name"], self)
            action.triggered.connect(lambda: print(f"{menu_item['name']} clicked"))
            menu.addAction(action)
            logger.debug(f"Action added for menu item: {menu_item['name']}")

    @staticmethod
    def run_gui():
        logger.info("Starting the GUI application.")
        app = QApplication(sys.argv)
        main_window = MainWindow()
        main_window.show()
        logger.info("GUI application started.")
        sys.exit(app.exec_())


if __name__ == "__main__":
    MainWindow()
