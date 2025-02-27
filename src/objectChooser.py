from PySide6.QtCore import Qt, QRect
from PySide6.QtWidgets import (
    QMainWindow,
    QDockWidget,
    QWidget,
    QLabel,
    QGridLayout,
    QVBoxLayout,
    QHBoxLayout,
    QSpacerItem,
    QSizePolicy,
    QApplication
)
from PySide6.QtGui import QPixmap, QScreen
import os


class objectChooser(QMainWindow):   
    def __init__(self, modelStore):
        super().__init__()
        
        self.path = "../../PlanetsAndMoons"
    
    def get_directories_list(path):
        if path is None:
            path = os.getcwd()
        return [entry for entry in os.listdir(path) if os.path.isdir(os.path.join(path, entry))]

    def list_objects(self):
        dir_list = self.get_directories_list("../../PlanetsAndMoons")
        return dir_list
    

    