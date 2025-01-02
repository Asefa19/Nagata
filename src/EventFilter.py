from PySide6.QtCore import QObject, QEvent
from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtGui import QPixmap

class EventFilter(QObject):
    def __init__(self):
        super(EventFilter, self).__init__()
        
    def buildCarousel(parent) -> QWidget:
        
        parent.carousel = QWidget()
        parent.carousel.setFixedSize(100,300)
        parent.carousel.show()
        
    def eventFilter(self, obj,event):
        if isinstance(obj,QLabel):
            if event.type() == QEvent.HoverEnter:
                print("Mouse  entered!")
                EventFilter.buildCarousel(self)
            elif event.type() == QEvent.HoverLeave:
                print("Mouse left!")
                # tray hides
        return super().eventFilter(obj, event)
    