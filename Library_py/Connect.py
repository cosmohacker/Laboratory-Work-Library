import sys

import mysql.connector
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QDialog, QDialogButtonBox, \
    QMessageBox, QListWidget, QHBoxLayout, QListWidgetItem

import Home
from utils import temp


class Connect(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Connect")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.window().setWindowIcon(QIcon('assets/icon.jpg'))

        self.txtHostName = QLineEdit(self)
        self.txtHostUsername = QLineEdit(self)
        self.txtHostDatabase = QLineEdit(self)
        self.txtHostPassword = QLineEdit(self)
        self.txtHostPassword.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(QLabel("Host Name:"))
        self.layout.addWidget(self.txtHostName)
        self.layout.addWidget(QLabel("Host Username:"))
        self.layout.addWidget(self.txtHostUsername)
        self.layout.addWidget(QLabel("Host Database:"))
        self.layout.addWidget(self.txtHostDatabase)
        self.layout.addWidget(QLabel("Host Password:"))
        self.layout.addWidget(self.txtHostPassword)

        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel | QDialogButtonBox.Apply, self)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        self.buttons.button(QDialogButtonBox.Apply).clicked.connect(self.test_connection)
        self.buttons.button(QDialogButtonBox.Ok).clicked.connect(self.save_connection)
        self.buttons.button(QDialogButtonBox.Cancel).clicked.connect(self.cancel_connection)
        self.layout.addWidget(self.buttons)

        self.setFixedSize(300, 350)

        self.txtHostName.setPlaceholderText("Enter host name")
        self.txtHostName.setText(temp.temp_host_name)
        self.txtHostUsername.setPlaceholderText("Enter host username")
        self.txtHostUsername.setText(temp.temp_host_username)
        self.txtHostDatabase.setPlaceholderText("Enter host database")
        self.txtHostDatabase.setText(temp.temp_host_database)
        self.txtHostPassword.setPlaceholderText("Enter host password")
        self.txtHostPassword.setText(temp.temp_host_password)

        self.table_layout = QHBoxLayout()
        self.layout.addLayout(self.table_layout)

        self.table_list = QListWidget(self)
        self.table_layout.addWidget(self.table_list)

    def closeEvent(self, event):
        self.home_window = QtWidgets.QMainWindow()
        self.ui = Home.Home()
        self.ui.setupUi(self.home_window)
        self.home_window.window().show()
        self.close()

    def save_connection(self):
        temp.temp_host_password = self.txtHostPassword.text()
        temp.temp_host_username = self.txtHostUsername.text()
        temp.temp_host_database = self.txtHostDatabase.text()
        temp.temp_host_name = self.txtHostName.text()
        self.home_window = QtWidgets.QMainWindow()
        self.ui = Home.Home()
        self.ui.setupUi(self.home_window)
        self.home_window.window().show()
        self.close()

    def cancel_connection(self):
        self.home_window = QtWidgets.QMainWindow()
        self.ui = Home.Home()
        self.ui.setupUi(self.home_window)
        self.home_window.window().show()
        self.close()

    def test_connection(self):
        host_name = self.txtHostName.text()
        host_username = self.txtHostUsername.text()
        host_database = self.txtHostDatabase.text()
        host_password = self.txtHostPassword.text()

        try:
            conn = mysql.connector.connect(
                host=host_name,
                user=host_username,
                password=host_password,
                database=host_database
            )

            QMessageBox.information(self, "Test Connection", "Connection successful!", QMessageBox.Ok)
            self.buttons.button(QDialogButtonBox.Ok).setEnabled(True)
            cursor = conn.cursor()
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            for table in tables:
                item = QListWidgetItem(table[0])
                self.table_list.addItem(item)

        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Test Connection", f"Connection failed: {str(e)}", QMessageBox.Ok)
            self.buttons.button(QDialogButtonBox.Ok).setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialog = Connect()
    if dialog.exec_() == QDialog.Accepted:
        host_name = dialog.txtHostName.text()
        host_username = dialog.txtHostUsername.text()
        host_database = dialog.txtHostDatabase.text()
        host_password = dialog.txtHostPassword.text()

        temp.temp_host_database = host_database
        temp.temp_host_name = host_name
        temp.temp_host_username = host_username
        temp.temp_host_password = host_password

    sys.exit(app.exec_())
