from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QHBoxLayout,
    QScrollArea,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

class ChatWidget(QWidget):
    user_Input = Signal(str)
    # history_Widget = QTextEdit()
    # prompt_Window = QTextEdit()
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        chatLayout = QVBoxLayout()
        chatLayout.setSpacing(0)
        
        # Top Half
        
        # ChatWidget.history_Widget.setReadOnly(True)
        # ChatWidget.history_Widget.setStyleSheet("background-color: lightgreen")
        # ChatWidget.history_Widget.setAlignment(Qt.AlignRight)
        
        self.history_Widget = QTextEdit()
        self.history_Widget.setReadOnly(True)
        self.history_Widget.setStyleSheet("background-color: lightgreen")
        self.history_Widget.setAlignment(Qt.AlignRight)
        
        self.history_Scroll = QScrollArea()
        self.history_Scroll.setWidget(self.history_Widget)
        self.history_Scroll.setWidgetResizable(True)
        
        
        chatLayout.addWidget(self.history_Scroll, stretch=1)
        
        # Bottom Half
        
        self.prompt_Window = QTextEdit()
        self.prompt_Window.setAlignment(Qt.AlignRight)
        self.prompt_Window.setFixedHeight(175)
        chatLayout.addWidget(self.prompt_Window, stretch=1)
        
        chatLayout.setAlignment(Qt.AlignRight)
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
            self.user_Input.emit(prompt)
            
            self.clear()
        else:
            super().keyPressEvent(event)