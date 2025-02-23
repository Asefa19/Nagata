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
        self.modelType = 0
        
    def buildCarousel(self, parent, build: bool) -> QWidget:    
        if build:
            
            carousel = QWidget()
            carousel.setGeometry(45, 85, 300, 600)
            carousel.option1 = QPushButton('Analysis Model')
            carousel.option2 = QPushButton('Analysis')
            carousel.option3 = QPushButton('What is this')

            layout = QVBoxLayout()
            layout.addWidget(carousel.option1)
            layout.addWidget(carousel.option2)
            layout.addWidget(carousel.option3)

            carousel.setLayout(layout)
            carousel.show()
        else:
            pass
      
        def on_Switch_Model():
            if carousel.option1.clicked:
                self.modelType = ModelStore.ModelStore.retrieveModel(self.modelType)
                if self.modelType == 0:
                    self.modelType = 1
                else:
                    self.modelType = 0 
                ModelStore.ModelStore.saveModel(self.modelType)
                #carousel.option1.setText("Report Model")
                #print("Report Model")
                #else:
                #    model_Selector.selected = 0
                #    model_Selector.select(0)
                #    carousel.option1.setText("Chat Model")
        
        def on_Data_Analyzer():
            global data_analyzer
            data_analyzer = DataAnalyzer()
            data_analyzer.show()
            
        def on_option3():
            carousel.close()
            
            
        carousel.option1.clicked.connect(on_Switch_Model)
        carousel.option2.clicked.connect(on_Data_Analyzer)
        carousel.option3.clicked.connect(on_option3)

        

        
        