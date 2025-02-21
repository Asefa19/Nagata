from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from DataAnalyzer import DataAnalyzer
import ModelStore

# Build in mainwindow instead of eventfilter,
# will make getting and sending info in and out a lot easier.

class Carousel(QWidget):
    def __init__(self, parent):
        Carousel.buildCarousel(self, parent)
        self.modelType = 0
        
        #super(Carousel, self).__init__()
        
    def buildCarousel(self, parent) -> QWidget:
        #model_Selector = ModelSelection()       
        
        parent.carousel = QWidget()
        parent.carousel.setGeometry(45, 85, 300, 600)
        parent.carousel.option1 = QPushButton('Analysis Model')
        parent.carousel.option2 = QPushButton('Analysis')
        parent.carousel.option3 = QPushButton('What is this')

        layout = QVBoxLayout()
        layout.addWidget(parent.carousel.option1)
        layout.addWidget(parent.carousel.option2)
        layout.addWidget(parent.carousel.option3)

        
        parent.carousel.setLayout(layout)
        parent.carousel.show()
        
      
        def on_Switch_Model():
            if parent.carousel.option1.clicked:
                self.modelType = ModelStore.ModelStore.retrieveModel(self.modelType)
                if self.modelType == 0:
                    self.modelType = 1
                else:
                    self.modelType = 0 
                ModelStore.ModelStore.saveModel(self.modelType)
                #parent.carousel.option1.setText("Report Model")
                #print("Report Model")
                #else:
                #    model_Selector.selected = 0
                #    model_Selector.select(0)
                #    parent.carousel.option1.setText("Chat Model")
        
        def on_Data_Analyzer():
            global data_analyzer
            data_analyzer = DataAnalyzer()
            data_analyzer.show()
            
        def on_option3():
            parent.carousel.close()
            
            
        parent.carousel.option1.clicked.connect(on_Switch_Model)
        parent.carousel.option2.clicked.connect(on_Data_Analyzer)
        parent.carousel.option3.clicked.connect(on_option3)

        

        
        