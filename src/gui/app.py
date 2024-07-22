import sys
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow


class PortfolioManagerApp:
    def __init__(self, menu_structure):
        self.app = QApplication(sys.argv)
        self.main_window = MainWindow(menu_structure)

    def run(self):
        self.main_window.show()
        sys.exit(self.app.exec_())
