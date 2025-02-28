from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QPushButton,
    QHBoxLayout,
    QWidget,
    QVBoxLayout,
    QLabel,
    QMenu,
    QMenuBar,
    QSizePolicy,
    QInputDialog,
    QApplication,
    QLineEdit,
    QMainWindow
)
from PySide6.QtGui import QAction
import matplotlib.pyplot as plt
from astroML.datasets import (fetch_sdss_spectrum, 
                              fetch_sdss_sspp, 
                              fetch_dr7_quasar, 
                              fetch_nasa_atlas)
from astroML.plotting import MultiAxes
from astropy.visualization import hist
import numpy as np
import tensorflow_datasets as tfds
import astro_datasets
import tensorflow as tf
import os
import shutil
import PIL
import sys


class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Another Window")
        layout = QVBoxLayout()
        label = QPushButton("This is another window.")
        layout.addWidget(label)
        self.setLayout(layout)
    
class objWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Obj Window")
          
        layout = QHBoxLayout()        
        self.plate_in = QLineEdit()
        plate_lbl = QLabel("plate")
        layout.addWidget(plate_lbl)
        layout.addWidget(self.plate_in)
        self.mjb_in = QLineEdit()
        mjb_lbl = QLabel("mjd")
        layout.addWidget(mjb_lbl)
        layout.addWidget(self.mjb_in)
        self.fiber_in = QLineEdit()
        fiber_lbl = QLabel("fiber")
        layout.addWidget(fiber_lbl)
        layout.addWidget(self.fiber_in)
        self.button = QPushButton("Enter")
        self.button.clicked.connect(self.get_text)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def get_text(self):
        plate_text = self.plate_in.text()
        mjb_text = self.mjb_in.text()
        fiber_text = self.fiber_in.text()
        print(f"text: {plate_text, mjb_text, fiber_text}")
        return plate_text, mjb_text, fiber_text 
                
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        
        menu = self.menuBar()
        file_menu = menu.addMenu("File")
        new_window_action = QAction("New Window", self)
        new_window_action.triggered.connect(self.open_new_window)
        file_menu.addAction(new_window_action)

    def open_new_window(self):
        self.new_window = AnotherWindow()
        self.new_window.show()
       
class DataAnalyzer(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.build_ui()
        self.setWindowTitle("Data Analyzer")
        self.resize(1920,1080)
        
    def build_ui(self):      
        self.setWindowTitle("Pulldown Menu Example")
        menu_bar = self.menuBar()     
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)      
        # create a Image Database menu
        iDatabase = menu_bar.addMenu("Image Database")
        planetary_objs_action = QAction("Planetary Objects", self)
        # add actions to menu
        iDatabase.addAction(planetary_objs_action)
        # connect actions
        planetary_objs_action.triggered.connect(self.planetary_objs)
        self.layout.setMenuBar(menu_bar)
            
    def planetary_objs(self):
        self.setWindowTitle("Another Window")
        layout = QVBoxLayout()
        label = QPushButton("This is another window.")
        layout.addWidget(label)
        self.setLayout(layout) 
        self.new_window = objWin()
        self.new_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = DataAnalyzer() #()MainWindow
    main_window.show()
    sys.exit(app.exec())
    