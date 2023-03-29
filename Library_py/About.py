from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QSizePolicy, QMessageBox
from PyQt5.QtGui import QDesktopServices, QFont, QIcon, QPixmap
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl, Qt, QDir, QProcess
from PyQt5 import QtCore
import sys


class Popup(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        self.setGeometry(0, 0, 600, 450)
        self.setMaximumSize(QtCore.QSize(600, 450))
        self.setStyleSheet("background-color: black;")
        self.window().setWindowIcon(QIcon('assets/icon.jpg'))

        label1 = QLabel("Group project created by:\nЯгизджан Явуз, Батухан Увер, Ібрахім Чагтюрк Караджан [KH-221ia.e]")
        label2 = QLabel("Programs used while creating the project:\nPyCharm, QtCreator, XAMPP, phpMyAdmin (MySQL)")
        label3 = QLabel("Ягизджан Явуз : Application, Database ")
        label4 = QLabel("Батухан Увер : Database Diagram According to Database")
        label5 = QLabel("Ібрахім Чагтюрк Караджан : Application Workflow According to Application")

        label1.setStyleSheet("color: green;")
        label2.setStyleSheet("color: green;")
        label3.setStyleSheet("color: green;")
        label4.setStyleSheet("color: green;")
        label5.setStyleSheet("color: green;")

        label1.setAlignment(Qt.AlignCenter)
        label2.setAlignment(Qt.AlignCenter)
        label3.setAlignment(Qt.AlignCenter)
        label4.setAlignment(Qt.AlignCenter)
        label5.setAlignment(Qt.AlignCenter)

        video_layout = QVBoxLayout()
        self.video_player = QMediaPlayer(self)
        self.video_widget = QVideoWidget(self)
        self.video_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.video_player.setVideoOutput(self.video_widget)
        self.video_player.setMedia(QMediaContent(QUrl.fromLocalFile("assets/drip_c0ck.mp4")))
        self.video_player.play()
        video_layout.addWidget(self.video_widget)
        video_layout.setContentsMargins(0, 0, 0, 0)
        video_layout.setSpacing(0)

        layout = QVBoxLayout()
        layout.addLayout(video_layout)
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)
        layout.addWidget(label5)

        button = QPushButton("Github")
        button.setStyleSheet("color: green;")
        button.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://www.github.com/cosmohacker")))

        layout.addWidget(button)
        layout.setAlignment(Qt.AlignCenter)

        self.setLayout(layout)

    def closeEvent(self, event):
        self.video_player.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    popup = Popup()
    popup.show()
    sys.exit(app.exec_())
