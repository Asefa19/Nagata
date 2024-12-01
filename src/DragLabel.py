from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt, QPoint

class DragLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.isDragging = False
        self.offset = QPoint()
    
    def mousePressEvent(self,event):
        if event.button() == Qt.LeftButton:
            self.isDragging = True
            self.offset = event.pos()
    
    def mouseMoveEvent(self, event):
        if self.isDragging:
            new_pos = self.parentWidget().mapFromGlobal(event.globalPos() - self.offset)
            self.move(new_pos)

    def mouseReleaseEvent(self, event):
        self.isDragging = False
