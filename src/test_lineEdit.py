from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout
from PySide6.QtWidgets import QLabel, QSizePolicy, QTextEdit, QPushButton
from PySide6.QtGui import QFontMetrics
from retrieveModel import set_model
from utils import filter_response
import sys


class chatWindow(QWidget):
    def __init__(self, llm_input, parent=None):
        super().__init__(parent)
        self.llm_input = llm_input
        self.setWindowTitle("NAGATA Chat Window")
        # set size of the window
        self.resize(1000, 300)
        
        # Line edit with a parent widget
        self.top_line_edit = QLineEdit(parent=self)
        self.top_line_edit.setStyleSheet("QTextEdit { border: none; }")
        
        # Push button for sending input to llm
        self.button = QPushButton("Submit")
        # empty label for are a where previous question printed
        self.label = QLabel("")
        # set up text edit for llm input placement
        self.bottom_line_edit = QTextEdit(
            self.llm_input, parent=self
        )
        self.bottom_line_edit.setStyleSheet("QTextEdit { border: none; }")
        self.bottom_line_edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        # make box readonly
        self.bottom_line_edit.setReadOnly(True)
        #bottom_line_edit.resize()
        self.bottom_line_edit.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        
        # create layout
        layout = QVBoxLayout()
        layout.addWidget(self.top_line_edit)
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addWidget(self.bottom_line_edit)
        self.setLayout(layout)

        # set button to send text
        self.button.clicked.connect(self.send_text)

    def send_text(self):
        text = self.top_line_edit.text()
        self.get_llm_response(text)
        
    def get_llm_response(self, text):
        # print user question
        self.label.setText(f"You entered: {text}") 
        # send user data to model
        llm_rsp = set_model(text)
        # filter llm output
        self.bottom_line_edit.setPlainText(filter_response(llm_rsp))


app = QApplication([])
llm_input = ''
window = chatWindow(llm_input=llm_input)
#window.adjust_text_area()
window.show()
app.exec()