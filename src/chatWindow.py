from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout
from PySide6.QtWidgets import QLabel, QSizePolicy, QTextEdit, QPushButton
from PySide6.QtGui import QFontMetrics
from retrieveModel import set_model
from utils import filter_response
import sys

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QHBoxLayout,
    QScrollArea,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

class chatWindow(QWidget):
    user_Input = Signal(str)
    # history_Widget = QTextEdit()
    # prompt_Window = QTextEdit()
    def __init__(self, llm_input, parent=None):
        super().__init__()
        self.llm_input = llm_input
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        chatLayout = QVBoxLayout()
        chatLayout.setSpacing(0)
        
        self.history_Widget = QTextEdit(
            self.llm_input, parent=self
        )
        self.history_Widget.setReadOnly(True)
        self.history_Widget.setStyleSheet("background-color: lightgreen")
        self.history_Widget.setAlignment(Qt.AlignRight)
        self.history_Widget.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.history_Widget.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        
        self.history_Scroll = QScrollArea()
        self.history_Scroll.setWidget(self.history_Widget)
        self.history_Scroll.setWidgetResizable(True)
        
        
        chatLayout.addWidget(self.history_Scroll, stretch=1)
        
        # Bottom Half
        
        self.prompt_Window = QTextEdit(self.llm_input, parent=self)
        self.prompt_Window.setAlignment(Qt.AlignRight)
        self.prompt_Window.setFixedHeight(175)
        chatLayout.addWidget(self.prompt_Window, stretch=1)
        
        # Push button for sending input to llm
        self.button = QPushButton("Submit")
        # empty label for are a where previous question printed
        self.label = QLabel("")
        
        self.button.clicked.connect(self.send_text)
        
        chatLayout.setAlignment(Qt.AlignRight)
        chatLayout.addWidget(self.button)
        chatLayout.addWidget(self.label)
        layout.addStretch(1)
        layout.addLayout(chatLayout)        
        layout.setAlignment(Qt.AlignmentFlag(Qt.AlignRight))
        
        self.resize(400,300)
        self.show()
      
    def getPrompt(self):
        return self.prompt_Window.toPlainText()
    
    def getResponse():
        response = 0
        return response
    
    def updateHistory():
        return
    
    def keyPressEvent(self, event):
        print("Key pressed:", event.key())
        if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
            prompt = self.getPrompt(self.prompt_Window)
            # self.user_Input.emit(prompt)
            self.get_llm_response(prompt)
            
            self.clear()
        else:

            super().keyPressEvent(event)
            
    def get_llm_response(self, text):
        # print user question
        self.label.setText(f"You entered: {text}") 
        # send user data to model
        llm_rsp = set_model(text)
        # filter llm output
        self.history_Widget.setPlainText(filter_response(llm_rsp))
    
    def send_text(self):
        text = self.history_Widget.toPlainText()
        self.get_llm_response(text)

# class chatWindow(QWidget):
#     def __init__(self, llm_input, parent=None):
#         super().__init__(parent)
#         self.setWindowTitle("NAGATA Chat Window")
#         # set size of the window
#         self.resize(1000, 300)
        
#         # Line edit with a parent widget
#         self.top_line_edit = QLineEdit(parent=self)
#         self.top_line_edit.setStyleSheet("QTextEdit { border: none; }")
        
        
#         # create layout
#         layout = QVBoxLayout()
#         layout.addWidget(self.top_line_edit)
#         layout.addWidget(self.label)
#         layout.addWidget(self.button)
#         layout.addWidget(self.bottom_line_edit)
#         self.setLayout(layout)

#         # set button to send text
#         self.button.clicked.connect(self.send_text)

        

if __name__ == '__main__':
    app = QApplication([])
    llm_input = ''
    window = chatWindow(llm_input=llm_input)
    # window.adjust_text_area()
    window.show()
    app.exec()