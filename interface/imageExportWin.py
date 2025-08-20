from PyQt6.QtWidgets import QDialog, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QComboBox, QFrame, QCheckBox, QLineEdit
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont

from .config import *
from export.image import ImageProcessor

class ImageExport(QDialog):
    def __init__(self, path):
        super().__init__()
        self.img = ImageProcessor(path)
        self.width, self.height = self.img.get_size

        self.setWindowTitle("Export as")
        self.setMinimumSize(QSize(300, 600))

        font = QFont(FONT_FAMILY, FONT_SIZE)
        self.setFont(font)

        main_l = QVBoxLayout()
        main_l.setSpacing(SPACING)

        #format
        format_l = QVBoxLayout()
        format_label = QLabel("format")
        select_export_format = QComboBox()
        select_export_format.addItems(['.png', '.jpg', 'bmp'])
        select_export_format.activated.connect(self.activated_format)

        line1 = QFrame()
        line1.setFrameShape(QFrame.Shape.HLine)

        format_l.addWidget(format_label)
        format_l.addWidget(select_export_format)
        format_l.addWidget(line1)

        #image size
        main_image_size_l = QVBoxLayout()
        image_size_label = QLabel("image size")

        image_width_l = QHBoxLayout()
        image_width_label = QLabel("width")
        image_width_edit = QLineEdit()
        image_width_edit.setText(str(self.width))
        image_width_l.addWidget(image_width_label)
        image_width_l.addWidget(image_width_edit)

        image_height_l = QHBoxLayout()
        image_height_label = QLabel("height")
        image_height_edit = QLineEdit()
        image_height_edit.setText(str(self.height))
        image_height_l.addWidget(image_height_label)
        image_height_l.addWidget(image_height_edit)

        line2 = QFrame()
        line2.setFrameShape(QFrame.Shape.HLine)

        main_image_size_l.addWidget(image_size_label)
        main_image_size_l.addLayout(image_width_l)
        main_image_size_l.addLayout(image_height_l)
        main_image_size_l.addWidget(line2)

        #Export/Cancel
        next_btns = QHBoxLayout()
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.cancel)
        export_btn = QPushButton("Export")
        export_btn.clicked.connect(self.export)
        next_btns.addWidget(cancel_btn)
        next_btns.addWidget(export_btn)

        main_l.addLayout(format_l)
        main_l.addLayout(main_image_size_l)
        main_l.addLayout(next_btns)
        main_l.addStretch()
        self.setLayout(main_l)

    def activated_format(self, index):
        if index == 0:
            pass
    
    def cancel(self):
        self.hide()

    def export(self):
        pass