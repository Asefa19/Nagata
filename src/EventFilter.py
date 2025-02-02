from PySide6.QtCore import QObject, QEvent
from PySide6.QtWidgets import QLabel, QWidget
from Carousel import *

class EventFilter(QObject):
    build = False
    
    def __init__(self):
        super(EventFilter, self).__init__()
    
    # instead of building carousel here, just return a bool that 
    # tells us whether or not we are hovering the tray. 
    def eventFilter(self, obj,event):
        if isinstance(obj,QLabel):
            if event.type() == QEvent.HoverEnter:
                # tray expands
                self.carousel = Carousel(self).__init__(self.carousel, self)
            elif event.type() == QEvent.HoverLeave:
                print("Mouse left!")
                # tray hides

        return super().eventFilter(obj, event)
    