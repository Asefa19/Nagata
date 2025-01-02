import sys
from MainWindow import *
from DragButton import DragButton
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QImage, QIcon, QScreen
from PySide6.QtWidgets import QApplication, QDockWidget, QWidget, QLabel, QVBoxLayout

app = QApplication([])
window = MainWindow()

screen = app.primaryScreen()
available_Geometry = screen.geometry()

height = (available_Geometry.height()-70)
width = (available_Geometry.width())

window.setFixedSize(width, height)

window.show()
app.exec()

