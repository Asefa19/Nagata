from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton,
                                 QMenu, QMenuBar, QWidget, QVBoxLayout)
from PySide6.QtGui import QAction
import sys

class objWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Obj Window")
        layout = QVBoxLayout(self)
        label = QPushButton("This is another window")
        layout.addWidget(label)
        self.setLayout(layout)
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        menu_bar = QMenuBar(self)
        file_menu = QMenu("File", self)
        menu_bar.addMenu(file_menu)

        new_window_action = QAction("New Window", self)
        new_window_action.triggered.connect(self.open_new_window)
        file_menu.addAction(new_window_action)

        self.setMenuBar(menu_bar)
        self.new_window = None 
    
    def open_new_window(self):
        self.new_window = objWin()
        self.new_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())