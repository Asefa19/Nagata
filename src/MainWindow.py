from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QDockWidget, QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        screen_Bounds = QApplication.primaryScreen().geometry()
        window_width = 900
        window_height = 800
        x = screen_Bounds.width() - window_width
        y = screen_Bounds.height() - window_height - screen_Bounds.y()
        
        self.setGeometry(x ,y, window_width, window_height)
                
        self.setWindowTitle("Nagata")

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        
                
