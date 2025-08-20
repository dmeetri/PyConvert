from PyQt6.QtWidgets import QMainWindow, QFileDialog, QWidget, QPushButton, QVBoxLayout, QScrollArea, QFrame, QLabel
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont
import os

from .config import *
from . import errorWin
from . import imageExportWin

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

        #Scroll
        self.all_files_scrol = QScrollArea()
        self.all_files_scrol.setWidgetResizable(True)

        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout()
        self.scroll_layout.setSpacing(SPACING)
        self.scroll_content.setLayout(self.scroll_layout)
        self.all_files_scrol.setWidget(self.scroll_content)
        
        #Base
        main_l = QVBoxLayout()
        main_l.setSpacing(BLOCK_SPACING)

        #Load files
        self.load_files_l = QVBoxLayout()
        self.load_files_l.setSpacing(SPACING)
        self.btn_load_file = QPushButton("Load files")
        self.btn_load_file.clicked.connect(self.load_files)
        self.load_files_l.addWidget(self.btn_load_file, alignment=Qt.AlignmentFlag.AlignTop)
        self.load_files_l.addWidget(self.all_files_scrol)
        self.load_files_l.addWidget(line)
        main_l.addLayout(self.load_files_l)

        #Convert files
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
            self.scroll_layout.addWidget(fl)
        
        self.clear_button.clicked.connect(self.clear_load_files)
        if self.load_files_l.indexOf(self.clear_button):
            self.load_files_l.addWidget(self.clear_button)

    def clear_load_files(self):
        self.file_path.clear()

        for i in reversed(range(self.scroll_layout.count())):
            widget = self.scroll_layout.itemAt(i).widget()
            if isinstance(widget, QLabel):
                self.scroll_layout.removeWidget(widget)
                widget.deleteLater()

        self.load_files_l.removeWidget(self.clear_button)
        self.clear_button.deleteLater()

    def convert_file_as(self):
        if not self.file_path:
            erw = errorWin.ErrorWindow("Missing files", "You have not selected files")
            erw.exec()
            return
        
        for img in self.file_path:
            iew = imageExportWin.ImageExport(img)
            iew.exec()