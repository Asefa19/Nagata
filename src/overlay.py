import sys
from MainWindow import MainWindow
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QApplication, QDockWidget, QWidget, QLabel, QVBoxLayout
app = QApplication([])
window = MainWindow()

screen_Bounds = app.primaryScreen().geometry()

dockWidget = QDockWidget(window)
# dockWidget.setFixedSize(75, 75)
dockWidget.setGeometry(0,0, 200, 1080)
dockTitle = QWidget(dockWidget) 
dockWidget.setTitleBarWidget(dockTitle) 
dockWidget.setAllowedAreas(Qt.LeftDockWidgetArea)
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

lbl_ChatHistory = QLabel(window)
lbl_ChatHistory.setStyleSheet("background-color: white;")
# lbl_ChatHistory.move(screen_Bounds.right()-window.width(), screen_Bounds.bottom()-window.height())

dock_Layout = QVBoxLayout()
dock_Layout.addWidget(lbl_Logo)
dockWidget.setLayout(dock_Layout)

layout = QVBoxLayout()
layout.addWidget(lbl_ChatHistory)
window.setLayout(layout)

window.show()
app.exec()