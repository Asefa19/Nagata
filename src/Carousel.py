from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QWidget
)
from ModelSelection import *
from DataAnalyzer import *

# Build in mainwindow instead of eventfilter,
# will make getting and sending info in and out a lot easier.

class Carousel(QWidget):
    def __init__(self, parent):
        Carousel.buildCarousel(self, parent)
        
        super(Carousel, self).__init__()
        
    def buildCarousel(self, parent) -> QWidget:
        
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
        
        parent.carousel.setLayout(layout)
        parent.carousel.show()
        
        def on_Switch_Model():
            if parent.carousel.option1.clicked:
                if model_Selector.selected == 0:
                    model_Selector.selected = 1
                    model_Selector.select(1)
                    print("Report Model")
                else:
                    model_Selector.selected = 0
                    model_Selector.select(0)
                    print("Analysis Model")
        
        def on_option2():
            global data_analyzer
            data_analyzer = DataAnalyzer()
            data_analyzer.show()
            
        parent.carousel.option1.clicked.connect(on_Switch_Model)
        parent.carousel.option2.clicked.connect(on_option2)

        
        