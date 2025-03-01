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
    def __init__(self, modelStore):
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
      
        # Event Filter
        self.e_filter = EventFilter()
        self.tray_Label.installEventFilter(self.e_filter)
        self.carousel = Carousel(modelStore)
        
        self.carousel.buildCarousel(self, True)
        self.carousel.setVisible(False)
        
        self.e_filter.build_Signal.connect(self.handleBuildSignal)
        self.e_filter.close_Signal.connect(self.handleCloseSignal)
        
    def handleBuildSignal(self, build: bool):
        # if build:
        #     if self.carousel and self.carousel.isEnabled():
        #         self.carousel.close_Carousel(self.carousel.isEnabled())
        #         print(self.carousel.isEnabled())
        #         self.carousel.buildCarousel(self, build)
        #     else:
        #         self.carousel.buildCarousel(self,build)
        #         self.carousel.setEnabled(True)
        #         print(self.carousel.isEnabled())
        # else: pass
        if build:
            if self.carousel and self.carousel.isVisible():
                self.carousel.setVisible(False)
                self.carousel.setVisible(True)
            elif self.carousel:
                self.carousel.setVisible(True)              
    
    def handleCloseSignal(self, close: bool):
        if close:
            self.carousel.close_Carousel()
        else: pass

    if __name__ == '__main__':
        app = QApplication([])
        window = chatWindow()
        window.show()
        app.exec()   
            