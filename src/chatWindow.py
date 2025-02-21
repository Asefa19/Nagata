from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout
from PySide6.QtWidgets import QLabel, QSizePolicy, QTextEdit, QPushButton
from PySide6.QtGui import QFontMetrics
from retrieveModel import set_model
from research_asst import research_asst
from chat_asst import chat_asst
import sys
import PromptTextEdit

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

    def __init__(self):
        super().__init__()
        # self.llm_input = llm_input
        layout = QHBoxLayout()
        self.setLayout(layout)
        self.ra = research_asst()
        self.ca = chat_asst()
        chatLayout = QVBoxLayout()
        chatLayout.setSpacing(0)
                
        self.history_Widget = QTextEdit(self)
        self.history_Widget.setReadOnly(True)
        self.history_Widget.setStyleSheet("background-color: lightgreen")
        self.history_Widget.setAlignment(Qt.AlignRight)
        self.history_Widget.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.history_Widget.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        
        self.history_Scroll = QScrollArea()
        self.history_Scroll.setWidget(self.history_Widget)
        self.history_Widget.setFixedWidth(380)
        #self.history_Scroll.setWidgetResizable(True)
        
        chatLayout.addWidget(self.history_Scroll, stretch=1)
        
        # Bottom Half
        self.prompt_Window = PromptTextEdit.PromptTextEdit()
        self.prompt_Window.setReadOnly(False)
        self.prompt_Window.setAlignment(Qt.AlignRight)
        chatLayout.addWidget(self.prompt_Window, stretch=1)
        
        # push button for sending input to llm
        self.button = QPushButton("Submit")
        # set button color to green
        self.button.setStyleSheet("background-color: rgb(0, 255, 25)")
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
        
    def get_llm_response(self, text):
        # print user question
        self.label.setText(f"You entered: {text}") 
        # send user data to model
        llm_rsp = self.ca.chat_asst(text)
        # llm output to history window
        print(llm_rsp)
        print(text)
        self.history_Widget.setPlainText(llm_rsp)
    
    def send_text(self):
        text = self.prompt_Window.toPlainText()
        self.prompt_Window.clear()
        self.get_llm_response(text)


# if __name__ == '__main__':
#     app = QApplication([])
#     window = chatWindow()
#     window.show()
#     app.exec()