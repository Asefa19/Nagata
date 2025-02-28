import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                               QMessageBox, QWidget, QVBoxLayout)
from PySide6.QtGui import QAction

class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Another Window")
        layout = QVBoxLayout()
        label = QPushButton("This is another window.")
        layout.addWidget(label)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        menu = self.menuBar()
        file_menu = menu.addMenu("File")
        new_window_action = QAction("New Window", self)
        new_window_action.triggered.connect(self.open_new_window)
        file_menu.addAction(new_window_action)

    def open_new_window(self):
         self.new_window = AnotherWindow()
         self.new_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())