from DragLabel import DragLabel
from Carousel import Carousel
from chatWindow import chatWindow
from llama_cpp import Llama
from EventFilter import EventFilter
from PySide6.QtCore import Qt, QRect
from PySide6.QtWidgets import (
    QMainWindow,
    QDockWidget,
    QWidget,
    QLabel,
    QGridLayout,
    QVBoxLayout,
    QHBoxLayout,
    QSpacerItem,
    QSizePolicy,
    QApplication
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

        # central_Layout = QVBoxLayout()
        self.central_Layout = QGridLayout()
        self.central_Layout.setContentsMargins(0, 0, 0, 0)
        self.central_Layout.setSpacing(1)
        
        # Tray for the overlay
        self.tray_Label = DragLabel()
        self.tray_Logo = "../../Nagata/assets/img/nagata_logo_40x39.png"
        self.pixmap = QPixmap(self.tray_Logo)

        if self.pixmap.isNull():
            print(f"Failed to load image from {self.tray_Logo}")

        else:
            self.tray_Label.setPixmap(self.pixmap)
            self.tray_Label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.tray_Label.setAttribute(Qt.WA_Hover, True)

        dock_Widget.setWidget(self.tray_Label)
        #self.chat = chatWindow()
        #self.chat.activateWindow()
        #self.chat.setFocus()
        #self.chat.setEnabled(True)
        
        #self.central_Layout.addWidget(self.chat,2,30)
        #self.central_Layout.addWidget(dock_Widget,1,0)

        #self.setFixedSize(self.central_Layout.sizeHint())
        #self.setLayout(self.central_Layout)
      
        # Event Filter
        self.e_filter = EventFilter()
        self.tray_Label.installEventFilter(self.e_filter)
        
        # self.chat.show()
        

    if __name__ == '__main__':
        app = QApplication([])
        window = chatWindow()
        window.show()
        app.exec()   
            