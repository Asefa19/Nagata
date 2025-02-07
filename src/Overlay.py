import sys
from MainWindow import MainWindow
from PySide6.QtWidgets import QApplication

app = QApplication([])
window = MainWindow()

screen = app.primaryScreen()
available_Geometry = screen.geometry()

height = (available_Geometry.height()-70)
width = (available_Geometry.width())

window.setFixedSize(width, height)

window.show()
app.exec()