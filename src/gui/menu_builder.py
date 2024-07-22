from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QMenuBar, QStatusBar


class MenuBuilder:
    def __init__(self, main_window, menu_structure):
        self.main_window = main_window
        self.menu_structure = menu_structure

    def create_menu(self):
        menubar = self.main_window.menuBar()
        self._add_menu_items(menubar, self.menu_structure['gui']['main_menu_items'])

    def _add_menu_items(self, parent_menu, items):
        for item in items:
            if item['available']:
                if 'sub_menu_items' in item and item['sub_menu_items']:
                    submenu = QMenu(item['name'], self.main_window)
                    self._add_menu_items(submenu, item['sub_menu_items'])
                    parent_menu.addMenu(submenu)
                else:
                    action = QAction(item['name'], self.main_window)
                    parent_menu.addAction(action)

    def create_status_bar(self):
        status_bar = self.main_window.statusBar()
        status_bar.showMessage('Ready')
        return status_bar
