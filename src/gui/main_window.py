from PyQt5.QtWidgets import QMainWindow
from gui_functions import GUIFunctions
from menu_builder import MenuBuilder
from styling import style_sheet


class MainWindow(QMainWindow):
    def __init__(self, menu_structure):
        super().__init__()
        self.setWindowTitle("Portfolio Manager")
        self.setGeometry(100, 100, 800, 600)
        self.gui_functions = GUIFunctions()
        self.menu_structure = menu_structure
        self.init_ui()

    def init_ui(self):
        # Apply styling
        self.setStyleSheet(style_sheet)

        # Create menu and status bar
        menu_builder = MenuBuilder(self, self.menu_structure)
        menu_builder.create_menu()
        menu_builder.create_status_bar()
