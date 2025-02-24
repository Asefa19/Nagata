from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QWidget,
    QVBoxLayout,
    QLabel
)

class WebReport(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.build_ui()
        
        self.setWindowTitle("Data Analyzer")
        self.resize(1920,1080)
        
    def build_ui(self):
        
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)
        
        
        self.setStyleSheet("""
                           QWidget{
                               background-color: #f0f0f0;
                               font-family: Arial;
                            }
                            QPushButton{
                                background-color: #0078d4;
                                color: white;
                                padding: 8px;
                                border-radius:4px;
                            }
                            """)
        
        
