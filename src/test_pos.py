
from PySide6.QtWidgets import  QApplication, QWidget, QPushButton
from PySide6.QtWidgets import QApplication, QWidget, QLabel
#from PyQt6 import QApplication, QWidget, QPushButton
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setGeometry(10, 10, 300, 200)  # x, y, width, height
window.setWindowTitle("QWidget Position Example")

label = QLabel("This is a QLabel", window)
label.move(50, 50)  # Using move() to set position (x, y)

label2 = QLabel("This is another QLabel", window)
label2.pos = (100, 100) #Using pos property to set position (x,y)

window.show()

sys.exit(app.exec())