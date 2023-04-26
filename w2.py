from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit

from PyQt5.QtCore import Qt


class UiMainTwo(QWidget):
    def __init__(self, title, text=None):
        super(UiMainTwo, self).__init__()
        self.setWindowTitle(title)
        self.resize(600, 600)
        self.initUI2(text)

    def initUI2(self, text):
        layout = QVBoxLayout()
        self.label1 = QTextEdit()
        self.label1.setPlainText(text)
        self.label1.setTextInteractionFlags(Qt.TextSelectableByMouse)
        layout.addWidget(self.label1)
        self.setLayout(layout)
