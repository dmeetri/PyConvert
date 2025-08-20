from PyQt6.QtWidgets import QMainWindow
from .editor_ui import Ui_MainWindow

from .errorWin import show_error
from .imageExportWin import ImageExport

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.actionExport_as.triggered.connect(self.open)

    def open(self):
        img = ImageExport("/Users/dmeetri/Pictures/шапка.jpg")
        img.exec()

'''    def load_files(self):
        self.file_path, _ = QFileDialog.getOpenFileNames(self, "Select files", "", "Images (*.png *.jpg *.jpeg *.bmp)")

        for i in range(len(self.file_path)):
            fl = QLabel(ImageProcessor(self.file_path[i]).get_name)
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
            show_error("Missing files", "You have not selected files")
            return
        
        for img in self.file_path:
            iew = imageExportWin.ImageExport(img)
            iew.exec()'''