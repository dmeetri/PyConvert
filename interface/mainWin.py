from PyQt6.QtWidgets import QMainWindow, QFileDialog, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont

from . import errorWin
from .config import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Edit")
        self.setMinimumSize(QSize(400, 600))

        central = QWidget()

        main_font = QFont(FONT_FAMILY, FONT_SIZE)
        central.setFont(main_font)

        main_l = QVBoxLayout()

        self.btn_load_file = QPushButton("Загрузить файл(ы)")
        self.btn_load_file.clicked.connect(self.load_files)
        self.btn_convert_file = QPushButton("Конвертировать")
        self.btn_convert_file.clicked.connect(self.convert_file_as)

        main_l.addWidget(self.btn_load_file, alignment=Qt.AlignmentFlag.AlignTop)
        main_l.addWidget(self.btn_convert_file, alignment=Qt.AlignmentFlag.AlignTop)
        main_l.addStretch()
        central.setLayout(main_l)

        self.setCentralWidget(central)

    def load_files(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Все файлы (*)")

    def convert_file_as(self):
        pass

    '''def open_jpeg_converter(self):
        erw = errorWin.ErrorWindow("Ошибка!", "ок")
        erw.exec()'''