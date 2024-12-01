from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QDockWidget, QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
from App import App

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.app = App()
        self.setWindowTitle("Nagata")
        
        # setGeometry
        screen_Bounds = QApplication.primaryScreen().geometry()
        window_width = 900
        window_height = 800
        x = screen_Bounds.width() - window_width
        y = screen_Bounds.height() - window_height - screen_Bounds.y()
        
        self.setGeometry(x ,y, window_width, window_height)
                
        # Transparency flags
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.setCentralWidget(self.app)

        
                
