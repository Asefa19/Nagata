from DragLabel import DragLabel
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QMainWindow, QDockWidget, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtGui import QPixmap, QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1920,1080)
        self.setBaseSize(1920, 1080)
        
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.central_Widget = QWidget(self)
        self.setCentralWidget(self.central_Widget)
        
        # Setup dock
        dock_Widget = QDockWidget(self)
        dock_Widget.setFeatures = dock_Widget.DockWidgetFeature.DockWidgetFloatable | dock_Widget.DockWidgetFeature.DockWidgetMovable
        self.addDockWidget(Qt.LeftDockWidgetArea, dock_Widget)
        
        central_Layout = QVBoxLayout()
        
        # self.tray_Button = DragButton()
        self.tray_Label = DragLabel()
        self.tray_Logo = "/Nagata/Nagata/assets/img/nagata_logo_40x39.png"
        self.pixmap = QPixmap(self.tray_Logo)

        if self.pixmap.isNull():
            print(f"Failed to load image from {self.tray_Logo}")

        else:
            self.tray_Label.setPixmap(self.pixmap)
            # self.tray_Label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            
        dock_Widget.setWidget(self.tray_Label)
        central_Layout.addWidget(dock_Widget)
        
        self.setLayout(central_Layout)

        self.top_spacer = QSpacerItem(20,40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        central_Layout.addItem(self.top_spacer)

        bottom_layout= QHBoxLayout()
        self.central_Widget.setLayout(bottom_layout)

        self.left_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        bottom_layout.addItem(self.left_spacer)

        chat_Widget = QWidget()
        chat_Widget.setStyleSheet("background-color: lightgreen;")
        chat_Label = QLabel("Hello World!", chat_Widget)
        
        chat_Label.setAlignment(Qt.AlignBottom | Qt.AlignRight)
        
        bottom_layout.addWidget(chat_Label) 
        bottom_layout.addWidget(chat_Widget)

        
    
