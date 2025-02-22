import sys
from MainWindow import MainWindow
from PySide6.QtWidgets import QApplication
from chatWindow import chatWindow

app = QApplication([])
window = MainWindow()

screen = app.primaryScreen()
available_Geometry = screen.geometry()

height = (available_Geometry.height()-70)
width = (available_Geometry.width())

window.setFixedSize(width, height)

window.show()
chat = chatWindow()
#chat.show()
#window.chat.show()
sys.exit(app.exec())

app = QApplication([])
window = chatWindow()
window.show()
app.exec()   
