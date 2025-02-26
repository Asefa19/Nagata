from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QInputDialog, QVBoxLayout

def get_input_from_dialog(parent=None, title="Input", label="Enter value:", default_value=""):
    """Opens an input dialog and returns the entered text or None if cancelled."""
    text, ok = QInputDialog.getText(parent, title, label, text=default_value)
    if ok:
        return text
    return None

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.button = QPushButton("Open Input Dialog", self)
        self.button.clicked.connect(self.on_button_click)

        layout = QVBoxLayout(self)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def on_button_click(self):
        """Opens the input dialog and prints the result."""
        result = get_input_from_dialog(self, "My Input Dialog", "Enter your name:")
        if result is not None:
            print("You entered:", result)
        else:
            print("Dialog cancelled")

if __name__ == '__main__':
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec()