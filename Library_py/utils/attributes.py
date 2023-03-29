from PyQt5.QtWidgets import QMessageBox, QApplication


class Dialogs:

    @staticmethod
    def error_dialog(Title, Text, Message):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setWindowTitle(Title)
        error_dialog.setText(Text)
        error_dialog.setInformativeText(Message)
        error_dialog.setStandardButtons(QMessageBox.Ok)
        error_dialog.exec_()


class Copy:

    @staticmethod
    def copy_label():
        return 0
