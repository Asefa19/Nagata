from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QMainWindow, QDockWidget, QWidget, QLabel
from PySide6.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nagata")
        self.setMinimumSize(QSize(1920,1080))
        self.setMaximumSize(QSize(3440,1440))
        self.setBaseSize(QSize(1920,1080))
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        
        
    
