from PySide6.QtCore import QObject, QEvent
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap

class EventFilter(QObject):
    def __init__(self):
        super(EventFilter, self).__init__()
        
    def eventFilter(self, obj,event):
        if isinstance(obj,QLabel):
            if event.type() == QEvent.HoverEnter:
                print("Mouse  entered!")
            elif event.type() == QEvent.HoverLeave:
                print("Mouse left!")
        return super().eventFilter(obj, event)