from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from DataAnalyzer import DataAnalyzer
from LocalReport import LocalReport
from NASADatabase import NASADatabase
from WebReport import WebReport
import ModelStore

# Build in mainwindow instead of eventfilter,
# will make getting and sending info in and out a lot easier.

class Carousel(QWidget):
    def __init__(self, modelStore: ModelStore):
        super().__init__()
        self.modelType = 0
        self.model_store = modelStore
        
    def buildCarousel(self, parent, build: bool) -> QWidget:    
        def on_Switch_Model():
            if carousel.option1.clicked:
                self.modelType = self.model_store.retrieveModel()
                     
                if self.modelType == 0:
                    self.modelType = 1
                    carousel.option1.setText('Switch to Analysis')
                    carousel.option2.setText('Local Reports')
                    carousel.option3.setText('Web Reports')
                    
                    carousel.option2.clicked.connect(on_LocalReports)
                    carousel.option3.clicked.connect(on_WebReports)
                    self.model_store.saveModel(self.modelType)            
                else:
                    self.modelType = 0 
                    carousel.option1.setText('Switch to Report')
                    carousel.option2.setText('Data Visualizer')
                    carousel.option3.setText('NASA Database')
                    
                    carousel.option2.clicked.connect(on_DataAnalyzer)
                    carousel.option3.clicked.connect(on_NASADatabase)
                    self.model_store.saveModel(self.modelType)
                    # carousel.close()

        def on_DataAnalyzer():
            global data_analyzer
            data_analyzer = DataAnalyzer()
            data_analyzer.show()
            
        def on_LocalReports():
            global local_reports
            local_reports = LocalReport()
            local_reports.show()
            
        def on_NASADatabase():
            global nasa_data 
            nasa_data = NASADatabase()
            nasa_data.show()
                        
        def on_WebReports():
            global web_reports
            web_reports = WebReport()
            web_reports.show()
                
        if build:
            
            carousel = QWidget()
            carousel.setGeometry(45, 85, 300, 600)
            carousel.option1 = QPushButton('Switch to Report')
            carousel.option2 = QPushButton('Data Visualizer')
            carousel.option3 = QPushButton('NASA Database')

            layout = QVBoxLayout()
            layout.addWidget(carousel.option1)
            layout.addWidget(carousel.option2)
            layout.addWidget(carousel.option3)

            carousel.setLayout(layout)
            carousel.show()
            carousel.option1.clicked.connect(on_Switch_Model)
            carousel.option3.clicked.connect(on_NASADatabase)
        else:
            pass    
    




