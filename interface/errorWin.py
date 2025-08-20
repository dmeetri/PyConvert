from PyQt6.QtWidgets import QMessageBox

def show_error(title="ERROR", text="Press 'OK' to close"):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Critical)  # красная иконка ошибки
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.setStandardButtons(QMessageBox.StandardButton.Ok)
    msg.exec()