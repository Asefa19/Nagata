from PySide6.QtCore import QObject, QEvent, Signal
from PySide6.QtWidgets import QLabel, QWidget
from Carousel import *

class EventFilter(QObject):
    build_Signal = Signal(bool)
    def __init__(self):
        super(EventFilter, self).__init__()
    
    def eventFilter(self, obj,event):
        if isinstance(obj,QLabel):
            if event.type() == QEvent.HoverEnter:
                # tray expands
                # self.carousel = Carousel(self).__init__(QWidget)
                print("Mouse entered!")
                self.build_Signal.emit(True)
            elif event.type() == QEvent.HoverLeave:
                print("Mouse left!")
                self.build_Signal.emit(False)
                
                # tray hides

        return super().eventFilter(obj, event)
    
    # def getBuild(self):
    #     return self.build
    