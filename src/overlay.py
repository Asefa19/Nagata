import sys
from MainWindow import MainWindow
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QApplication, QDockWidget, QWidget, QLabel, QVBoxLayout
app = QApplication([])
window = MainWindow()

main_Layout = QVBoxLayout()
main_Layout.setAlignment(Qt.AlignLeft|Qt.AlignBottom)

screen_Bounds = app.primaryScreen().geometry()
window_width = 900
window_height = 800
x = screen_Bounds.width() - window_width
y = screen_Bounds.height() - window_height - screen_Bounds.y()

dockWidget = QDockWidget(window)
dockWidget.setWindowFlags(Qt.FramelessWindowHint)
dockWidget.setAttribute(Qt.WA_TranslucentBackground)
# dockWidget.setFixedSize(75, 75)
# dockWidget.setGeometry(0,0, 200, 1080)
# dockTitle = QWidget(dockWidget) 
# dockWidget.setTitleBarWidget(dockTitle) 
# dockWidget.setAllowedAreas(Qt.LeftDockWidgetArea)
# dockWidget.toggleViewAction()
# dockWidget.setFloating(True)

trayIcon = "/Nagata/Nagata/assets/img/nagata_logo_40x39.png"
lbl_Logo = QLabel(dockWidget)
pixmap = QPixmap(trayIcon)

image = pixmap.toImage()
# size = QSize(114,110)
# scaled_image = image.scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
scaled_pixmap = QPixmap.fromImage(image)

if pixmap.isNull():
    print(f"Failed to load image from {trayIcon}")

else:
    lbl_Logo.setPixmap(scaled_pixmap)
    lbl_Logo.setAlignment(Qt.AlignCenter)
    # lbl_Logo.setGeometry(0,0,75,75)

# lbl_ChatHistory = QLabel(window)
# lbl_ChatHistory.setStyleSheet("background-color: white;")
# lbl_ChatHistory.move(screen_Bounds.right()-window.width(), screen_Bounds.bottom()-window.height())

dock_Layout = QVBoxLayout()
dock_Layout.addWidget(lbl_Logo)
dockWidget.setLayout(dock_Layout)


main_Layout.addWidget(lbl_Logo)

chat_HistoryLabel = QLabel()
chat_HistoryLabel.setBaseSize(900,800)

"""
    Handle user input
    Take user microphone input, transcribe it to the prompt
    Reply appropriately. Append reply to QLabel
"""
# user_InputDevice = some device
# model.prompt = user_InputDevice.stream(?)
# prompt = model.prompt
# model.reply(prompt, text_out=chat_HistoryLabel)

chat_HistoryLabel.setStyleSheet("background-color : light-gray; color : black;")
chat_HistoryLabel.setText("Hello World!")

main_Layout.addWidget(chat_HistoryLabel)
window.setLayout(main_Layout) 

window.show()
app.exec()