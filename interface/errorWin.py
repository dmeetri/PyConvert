from PyQt6.QtWidgets import QDialog, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtCore import QSize

class ErrorWindow(QDialog):
    def __init__(self, title: str = "ERROR", 
                 err: str = "Нажмите 'ok' чтобы закрыть окно"):
        super().__init__()

        self.setWindowTitle(title)
        self.setMinimumSize(QSize(200, 100))

        self.label = QLabel(err)
        self.button = QPushButton("ok")
        self.button.clicked.connect(self.accept)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)