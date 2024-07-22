# styling.py


def set_styling(widget):
    """Set the styling for the application."""
    widget.setStyleSheet(
        """
        QMainWindow {
            --background-color: #f7f7f7;
            --text-color: #333333;
            --border-color: #dcdcdc;
            --hover-background-color: #f0f0f0;
            --pressed-background-color: #e6e6e6;
            background-color: var(--background-color);
            font-family: Arial, Helvetica, sans-serif;
        }
        QMenuBar {
            background-color: #ffffff;
            color: var(--text-color);
            padding: 5px;
            border-bottom: 1px solid var(--border-color);
        }
        QMenuBar::item {
            background-color: #ffffff;
            color: var(--text-color);
            padding: 5px 10px;
            margin: 0 5px;
            border-radius: 4px;
        }
        QMenuBar::item::selected {
            background-color: var(--hover-background-color);
        }
        QMenu {
            background-color: #ffffff;
            color: var(--text-color);
            border: 1px solid var(--border-color);
            border-radius: 4px;
        }
        QMenu::item {
            padding: 5px 10px;
        }
        QMenu::item::selected {
            background-color: var(--pressed-background-color);
        }
        QAction {
            color: var(--text-color);
        }
        QPushButton {
            background-color: #ffffff;
            color: var(--text-color);
            padding: 8px 16px;
            border: 1px solid var(--border-color);
            border-radius: 4px;
            margin: 5px;
        }
        QPushButton:hover {
            background-color: var(--hover-background-color);
        }
        QPushButton:pressed {
            background-color: var(--pressed-background-color);
        }
    """
    )
