import sys
from MainWindow import MainWindow
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QApplication, QDockWidget, QWidget, QLabel, QVBoxLayout

app = QApplication([])
window = MainWindow()

"""
    Handle user input
    Take user microphone input, transcribe it to the prompt
    Reply appropriately. Append reply to QLabel
"""
# user_InputDevice = some device
# model.prompt = user_InputDevice.stream(?)
# prompt = model.prompt
# model.reply(prompt, text_out=chat_HistoryLabel)

window.show()
app.exec()