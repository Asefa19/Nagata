from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QMainWindow, QDockWidget, QWidget, QPushButton
from DragButton import DragButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nagata")
        self.setMinimumSize(QSize(800,600))
        self.setMaximumSize(QSize(3440,1440))
        self.setBaseSize(QSize(1920,1080))
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        dockWidget = QDockWidget(self)
        dockTitle = QWidget(dockWidget)
        dockWidget.setTitleBarWidget(dockTitle)
        button = DragButton("Drag", dockWidget)
        dockWidget._button = DragButton(button)

    
