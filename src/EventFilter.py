from PySide6.QtCore import QObject, QEvent, Signal
from PySide6.QtWidgets import QLabel, QWidget
from Carousel import *

class EventFilter(QObject):
    build_Signal = Signal(bool)
    close_Signal = Signal(bool)
    
    def __init__(self):
        super(EventFilter, self).__init__()
    
    def eventFilter(self, obj,event):
        # Open carousel
        if isinstance(obj,QLabel):
            if event.type() == QEvent.HoverEnter:
                # tray expands
                # self.carousel = Carousel(self).__init__(QWidget)
                print("Mouse entered!")
                self.build_Signal.emit(True)
            elif event.type() == QEvent.HoverLeave:
                print("Mouse left!")
                self.build_Signal.emit(False)
        # Close carousel
        if isinstance(obj, Carousel):
            if event.type() == QEvent.HoverEnter:
                print('Enter car')
                self.close_Signal.emit(False)
            elif event.type() == QEvent.HoverLeave:
                print('Exit car')
                self.close_Signal.emit(True)
        return super().eventFilter(obj, event)
    
    # def getBuild(self):
    #     return self.build
    