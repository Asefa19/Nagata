from PySide6.QtWidgets import QTextEdit
from PySide6.QtCore import Qt

class PromptTextEdit(QTextEdit):
    prompt = ""
    def keyPressEvent(self, event):
        print("Key pressed:", event.key())
        if self.hasFocus():
            
            if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
                self.prompt = self.toPlainText()
                # self.user_Input.emit(prompt)
                # self.send_text(prompt)
            
                self.clear()
                print(self.prompt)
            else:
                super().keyPressEvent(event)
            
    def getPrompt(self):
        return self.prompt
    # def send_text(self):
    #     text = self.getPrompt(self)
        
    # def get_llm_response(self, text):
    # # print user question
    # self.label.setText(f"You entered: {text}") 
    # # send user data to model
    # llm_rsp = set_model(text)
    # # filter llm output
    # self.history_Widget.setPlainText(filter_response(llm_rsp))