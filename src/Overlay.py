import sys
from MainWindow import MainWindow
from PySide6.QtWidgets import QApplication
from chatWindow import chatWindow
from ModelStore import ModelStore


app = QApplication([])
model_store = ModelStore()
window = MainWindow(model_store)

screen = app.primaryScreen()
available_Geometry = screen.geometry()

height = (available_Geometry.height()-70)
width = (available_Geometry.width())

window.setFixedSize(width, height)
window.show()

chat = chatWindow(model_store)
print(width, height)
chat.setGeometry(1920, 100, 400, 800)
sys.exit(app.exec())
  
