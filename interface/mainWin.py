from PyQt6.QtWidgets import QMainWindow, QFileDialog, QWidget, QPushButton, QVBoxLayout, QFrame, QLabel
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont
import os

from . import errorWin
from .config import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.file_path = []

        self.setWindowTitle("Image Edit")
        self.setMinimumSize(QSize(400, 600))

        main_font = QFont(FONT_FAMILY, FONT_SIZE)
        self.small_font = QFont(FONT_FAMILY, SMALL_FONT_SIZE)
        self.clear_button = QPushButton("Delete all")

        central = QWidget()
        central.setFont(main_font)

        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)

        self.name_load_files_l = QVBoxLayout()

        main_l = QVBoxLayout()
        main_l.setSpacing(BLOCK_SPACING)

        self.load_files_l = QVBoxLayout()
        self.load_files_l.setSpacing(SPACING)
        self.btn_load_file = QPushButton("Load files")
        self.btn_load_file.clicked.connect(self.load_files)
        self.load_files_l.addWidget(self.btn_load_file, alignment=Qt.AlignmentFlag.AlignTop)
        self.load_files_l.addLayout(self.name_load_files_l)
        self.load_files_l.addWidget(line)
        main_l.addLayout(self.load_files_l)

        convert_files_l = QVBoxLayout()
        convert_files_l.setSpacing(SPACING)
        self.btn_convert_file = QPushButton("Export")
        self.btn_convert_file.clicked.connect(self.convert_file_as)
        convert_files_l.addWidget(self.btn_convert_file, alignment=Qt.AlignmentFlag.AlignTop)
        main_l.addLayout(convert_files_l)

        main_l.addStretch()
        central.setLayout(main_l)

        self.setCentralWidget(central)

    def load_files(self):
        self.file_path, _ = QFileDialog.getOpenFileNames(self, "Select files", "", "Images (*.png *.jpg *.jpeg *.bmp)")

        for i in range(len(self.file_path)):
            fl = QLabel(os.path.basename(self.file_path[i]))
            fl.setFont(self.small_font)
            self.name_load_files_l.addWidget(fl)
        
        
        self.clear_button.clicked.connect(self.clear_load_files)
        self.load_files_l.addWidget(self.clear_button)

    def clear_load_files(self):
        self.file_path.clear()

        for i in reversed(range(self.name_load_files_l.count())):
            widget = self.name_load_files_l.itemAt(i).widget()
            if isinstance(widget, QLabel):
                self.name_load_files_l.removeWidget(widget)
                widget.deleteLater()

        self.load_files_l.removeWidget(self.clear_button)
        self.clear_button.deleteLater()

    def convert_file_as(self):
        if len(self.file_path) == 0:
            erw = errorWin.ErrorWindow("Missing files", "You have not selected files")
            erw.exec()
            return

    '''def open_jpeg_converter(self):
        erw = errorWin.ErrorWindow("Ошибка!", "ок")
        erw.exec()'''