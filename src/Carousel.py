from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QWidget
)

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
        
        parent.carousel.setLayout(layout)
        parent.carousel.show()