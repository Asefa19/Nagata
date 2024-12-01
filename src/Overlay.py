import sys
from MainWindow import MainWindow
from DragButton import DragButton
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QImage, QIcon
from PySide6.QtWidgets import QApplication, QDockWidget, QWidget, QLabel, QVBoxLayout

app = QApplication([])
window = MainWindow()

window.show()
app.exec()
