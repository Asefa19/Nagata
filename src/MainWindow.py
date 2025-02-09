from DragLabel import DragLabel
from ModelSelection import ModelSelection
from Carousel import Carousel
from ChatWidget import *
from EventFilter import EventFilter
from PySide6.QtCore import Qt, QRect
from PySide6.QtWidgets import (
    QMainWindow,
    QDockWidget,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QSpacerItem,
    QSizePolicy,
    QTextEdit
)
from PySide6.QtGui import QPixmap, QScreen


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        # Transparency Flags
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.central_Widget = QWidget(self)
        self.setCentralWidget(self.central_Widget)

        # Setup dock
        dock_Widget = QDockWidget(self)
        dock_Widget.setFeatures = (
            dock_Widget.DockWidgetFeature.DockWidgetFloatable
            | dock_Widget.DockWidgetFeature.DockWidgetMovable
        )
        self.addDockWidget(Qt.LeftDockWidgetArea, dock_Widget)

        central_Layout = QVBoxLayout()

        # Tray for the overlay
        self.tray_Label = DragLabel()
        self.tray_Logo = "../assets/img/nagata_logo_40x39.png"
        self.pixmap = QPixmap(self.tray_Logo)

        if self.pixmap.isNull():
            print(f"Failed to load image from {self.tray_Logo}")

        else:
            self.tray_Label.setPixmap(self.pixmap)
            self.tray_Label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.tray_Label.setAttribute(Qt.WA_Hover, True)

        dock_Widget.setWidget(self.tray_Label)
        central_Layout.addWidget(dock_Widget)

        self.setLayout(central_Layout)

        # Setup chat_History

        # spacers aren't what I imagined them to be. Look into making the label visible,
        # with background behind

        self.top_spacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )
        central_Layout.addItem(self.top_spacer)

        bottom_layout = QHBoxLayout()
        self.central_Widget.setLayout(bottom_layout)

        self.left_spacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )
        bottom_layout.addItem(self.left_spacer)
        
        chat_Widget = ChatWidget()
        chat_Widget.setStyleSheet("background-color: white;")
        bottom_layout.addWidget(chat_Widget)
        chat_Widget.setFocus()

        self.e_filter = EventFilter()
        self.tray_Label.installEventFilter(self.e_filter)
    
        self.prompt = None
        
        chat_Widget.user_Input.connect(self.on_User_Input)
        
    def on_User_Input(self, input):
        self.prompt = input
        print(self.prompt)

        
        