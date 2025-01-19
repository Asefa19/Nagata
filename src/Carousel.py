from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QWidget
)
from ModelSelection import *

# Build in mainwindow instead of eventfilter,
# will make getting and sending info in and out a lot easier.

class Carousel(QWidget):
    def __init__(self, parent):
        Carousel.buildCarousel(parent)
        
        super(Carousel, self).__init__()
        
    def buildCarousel(parent) -> QWidget:
        
        parent.carousel = QWidget()
        parent.carousel.setFixedSize(100,300)
        parent.carousel.option1 = QPushButton()
        parent.carousel.option2 = QPushButton()
        parent.carousel.option3 = QPushButton()
        
        layout = QVBoxLayout()
        layout.addWidget(parent.carousel.option1)
        layout.addWidget(parent.carousel.option2)
        layout.addWidget(parent.carousel.option3)
        
        model_Selector = ModelSelection()
        selected = 0
        if parent.carousel.option1.pressed():
            if selected == 0:
                model_Selector.select(1)
                selected = 1
            else:
                model_Selector.select(0)
                selected = 0
        
        parent.carousel.setLayout(layout)
        parent.carousel.show()