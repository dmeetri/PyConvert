from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton
from PyQt6.QtCore import QSize

from . import errorWin

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Edit")
        self.setMinimumSize(QSize(400, 600))

        button = QPushButton("Press Me!")
        button.clicked.connect(self.open_jpeg_converter)

        

        self.setCentralWidget(button)

    def open_jpeg_converter(self):
        erw = errorWin.ErrorWindow("Ошибка!", "ок")
        erw.exec()