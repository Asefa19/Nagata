import sys
from MainWindow import MainWindow
from PySide6.QtWidgets import QApplication
from chatWindow import chatWindow

app = QApplication([])
window = MainWindow()
# chat = chatWindow()
screen = app.primaryScreen()
available_Geometry = screen.geometry()

height = (available_Geometry.height()-70)
width = (available_Geometry.width())

window.setFixedSize(width, height)

window.show()
window.chat.show()
app.exec()