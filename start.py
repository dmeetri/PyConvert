from PyQt6.QtWidgets import QApplication
import sys

from interface import mainWin

def run():
    app = QApplication(sys.argv)

    win = mainWin.MainWindow()
    win.show()

    app.exec()

if __name__ == "__main__":
    run()
