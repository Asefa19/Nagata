from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout
from PySide6.QtWidgets import QLabel, QSizePolicy, QTextEdit, QPushButton
from ModelStore import ModelStore
from research_asst import research_asst
from chat_asst import chat_asst
import sys
import PromptTextEdit
from PySide6.QtGui import QFont
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

    def __init__(self, store):
        super().__init__()

        layout = QHBoxLayout()
        self.setLayout(layout)
        chatLayout = QVBoxLayout()
        chatLayout.setSpacing(0)
        
        # font size
        font = QFont()
        font.setPointSize(11)  # Set the font size
        
        # model obj
        self.ra = research_asst()
        self.ca = chat_asst()
        self.store = store
        # history
        self.history_label = QLabel("LLM Response")
        chatLayout.addWidget(self.history_label)
        self.history_Widget = QTextEdit(self)
        self.history_Widget.setReadOnly(True)
        self.history_Widget.setFont(font)
        self.history_Widget.setStyleSheet("background-color: lightgreen")
        self.history_Widget.setAlignment(Qt.AlignRight)
        self.history_Widget.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.history_Widget.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        
        # Scroll area
        self.history_Scroll = QScrollArea()
        self.history_Scroll.setWidget(self.history_Widget)
        self.history_Widget.setFixedSize(400, 300)
        chatLayout.addWidget(self.history_Scroll, stretch=1)
        
        # Bottom Half
        self.prompt_label = QLabel("User Input")
        chatLayout.addWidget(self.prompt_label)
        self.prompt_Window = PromptTextEdit.PromptTextEdit()
        self.prompt_Window.setReadOnly(False)
        self.prompt_Window.setAlignment(Qt.AlignLeft)
        self.prompt_Window.setFont(font)
        self.prompt_Window.setFixedSize(400, 100) 
        chatLayout.addWidget(self.prompt_Window, stretch=1)
       
        # push button for sending input to llm
        self.button = QPushButton("Submit")
        # set button color to green
        self.button.setStyleSheet("background-color: rgb(0, 255, 25)")
        self.label = QLabel("")       
        self.button.clicked.connect(self.send_text)
                   
        self.userInput = QTextEdit(self)
        self.userInput.setReadOnly(True)
        self.userInput.setStyleSheet(f"background-color: rgb({220}, {220}, {220});")
        self.userInput.setAlignment(Qt.AlignLeft)
        self.userInput.setFixedSize(400, 100) 
        self.userInput.setFont(font)
        self.userInput.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.userInput.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
    
        chatLayout.setAlignment(Qt.AlignRight)
        chatLayout.addWidget(self.button)
        chatLayout.addWidget(self.userInput)
        layout.addStretch(1)
        layout.addLayout(chatLayout)        
        layout.setAlignment(Qt.AlignmentFlag(Qt.AlignRight))

        self.resize(400,600)
        self.move(800, 20)
        self.show()

    def get_llm_response(self, text):
        # print user question
        self.userInput.setText(f"You entered: {text}") 
        # send user data to model
        modelType = self.store.retrieveModel()
        print('Chat window retrieve', modelType)
        if modelType == 0:
            print("chat model")
            llm_rsp = self.ca.chat_asst(text)
        elif modelType == 1:
            print("research model")
            llm_rsp = self.ra.research_asst(text)        # llm output to history window
        else:
            print('error catch')
        print(llm_rsp)
        print(text)
        self.history_Widget.setPlainText(llm_rsp)
    
    def send_text(self):
        text = self.prompt_Window.toPlainText()
        self.prompt_Window.clear()
        self.get_llm_response(text)

if __name__ == '__main__':
    app = QApplication([])
    model_store = ModelStore()

    screen = app.primaryScreen()
    available_Geometry = screen.geometry()
    height = (available_Geometry.height()-70)
    width = (available_Geometry.width())
    
    chat = chatWindow(model_store)
    chat.setGeometry(1920, 40, 400, 800)
    chat.show()
    app.exec()