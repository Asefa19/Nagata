from App import App
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QMainWindow, QDockWidget, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1920,1080)
        self.setBaseSize(1920, 1080)
        
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.app_Widget = App()
        
        
        self.central_Widget = QWidget(self)
        self.setCentralWidget(self.central_Widget)

        dock_Widget = QDockWidget(self)
        dock_Widget.setWidget(self.app_Widget)
        
        self.addDockWidget(Qt.LeftDockWidgetArea, dock_Widget)
        
        central_Layout = QVBoxLayout()
        self.central_Widget.setLayout(central_Layout)

        # self.top_spacer = QSpacerItem(20,40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        # central_Layout.addItem(self.top_spacer)

        # bottom_layout= QHBoxLayout()
        # self.central_Widget.setLayout(bottom_layout)

        # self.left_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # bottom_layout.addItem(self.left_spacer)

        # chat_Widget = QWidget()
        # chat_Widget.setStyleSheet("background-color: lightgreen;")
        # chat_Label = QLabel("Hello World!", chat_Widget)
        
        # bottom_layout.addWidget(chat_Label) 
        # bottom_layout.addWidget(chat_Widget)

        
    
