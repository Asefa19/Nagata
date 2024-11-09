from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nagata")

        self.setMinimumSize(QSize(800, 600))
        self.setMaximumSize(QSize(3440, 1440))
        self.setBaseSize(QSize(1920, 1080))

        self.setStyleSheet("""
            background-color: #00FFFFFF;
            color: #FFFFFF;
            font-family: Paladins Regular;
            font-size: 18px    
            """)

