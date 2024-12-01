import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap
from DragLabel import DragLabel

class App(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.main_Layout = QVBoxLayout()
        self.tray_Widget = QWidget()
        self.tray_Label = DragLabel()
        self.tray_Logo = "/Nagata/Nagata/assets/img/nagata_logo_40x39.png"
        self.pixmap = QPixmap(self.tray_Logo)

        if self.pixmap.isNull():
            print(f"Failed to load image from {self.tray_Logo}")

        else:
            self.tray_Label.setPixmap(self.pixmap)
            self.tray_Label.setAlignment(Qt.AlignLeft)

        # Init layout     
        self.main_Layout.addWidget(self.tray_Label)
        self.main_Layout.addWidget(self.tray_Widget)

        self.setLayout(self.main_Layout)

