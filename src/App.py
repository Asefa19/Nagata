import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QIcon
from DragButton import DragButton
from DragLabel import DragLabel

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.main_Layout = QVBoxLayout()
        
        self.dock_Widget = QDockWidget(self)
        
        # self.tray_Button = DragButton()
        self.tray_Label = DragLabel()
        self.tray_Logo = "/Nagata/Nagata/assets/img/nagata_logo_40x39.png"
        self.pixmap = QPixmap(self.tray_Logo)
        self.tray_Icon = QIcon(self.pixmap)

        if self.pixmap.isNull():
            print(f"Failed to load image from {self.tray_Logo}")

        else:
            # self.tray_Button.setIcon(self.tray_Icon)
            # self.tray_Button.setIconSize(self.pixmap.size())
            self.tray_Label.setPixmap(self.pixmap)
        
        # self.dock_Widget.setWidget(self.tray_Button)
        self.dock_Widget.setWidget(self.tray_Label)

        self.main_Layout.addWidget(self.dock_Widget)
        self.setLayout(self.main_Layout)
    