from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class Instructions(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Instructions")
        self.setGeometry(100, 100, 400, 130)
        self.setMaximumSize(QtCore.QSize(400, 130))
        self.resize(400, 130)
        self.window().setWindowIcon(QIcon('assets/icon.jpg'))
        delete_label = QLabel("To delete record from table double click the row", self)
        delete_label.setAlignment(Qt.AlignCenter)
        delete_label.setGeometry(10, 10, 380, 30)
        edit_label = QLabel("To select for edit edit record click one time to record", self)
        edit_label.setAlignment(Qt.AlignCenter)
        edit_label.setGeometry(10, 50, 380, 30)
        uid_label = QLabel("To get Unique Id Column Value Click UID row and ctrl+c", self)
        uid_label.setAlignment(Qt.AlignCenter)
        uid_label.setGeometry(10, 90, 380, 30)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    popup = Instructions()
    popup.show()
    sys.exit(app.exec_())
