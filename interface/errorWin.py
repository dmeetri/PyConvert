from PyQt6.QtWidgets import QDialog, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QFont

from .config import *

class ErrorWindow(QDialog):
    def __init__(self, title: str = "ERROR", 
                 err: str = "Press 'OK' for close"):
        super().__init__()

        self.setWindowTitle(f"ERROR: {title}")
        self.setMinimumSize(QSize(200, 100))

        font = QFont(FONT_FAMILY, FONT_SIZE)

        layout = QVBoxLayout()
        self.setFont(font)

        self.label = QLabel(err)
        self.button = QPushButton("OK")
        self.button.clicked.connect(self.accept)

        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)