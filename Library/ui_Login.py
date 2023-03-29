# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(500, 500)
        Widget.setStyleSheet(u"background-color: rgb(31, 33, 34);")
        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(85, 114, 311, 251))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(20)
        font.setBold(True)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lblAdministrator = QLabel(self.frame)
        self.lblAdministrator.setObjectName(u"lblAdministrator")
        self.lblAdministrator.setGeometry(QRect(50, 30, 141, 31))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setUnderline(True)
        self.lblAdministrator.setFont(font1)
        self.lblLogin = QLabel(self.frame)
        self.lblLogin.setObjectName(u"lblLogin")
        self.lblLogin.setGeometry(QRect(190, 30, 60, 31))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setUnderline(False)
        self.lblLogin.setFont(font2)
        self.lblLogin.setStyleSheet(u"color: rgb(156, 0, 0);")
        self.btnLogin = QPushButton(self.frame)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setGeometry(QRect(110, 210, 71, 24))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(12)
        self.btnLogin.setFont(font3)
        self.txtUsername = QLineEdit(self.frame)
        self.txtUsername.setObjectName(u"txtUsername")
        self.txtUsername.setGeometry(QRect(50, 110, 191, 24))
        self.lblUsername = QLabel(self.frame)
        self.lblUsername.setObjectName(u"lblUsername")
        self.lblUsername.setGeometry(QRect(50, 90, 81, 16))
        self.lblUsername.setFont(font3)
        self.txtPassword = QLineEdit(self.frame)
        self.txtPassword.setObjectName(u"txtPassword")
        self.txtPassword.setGeometry(QRect(50, 160, 191, 24))
        self.lblPassword = QLabel(self.frame)
        self.lblPassword.setObjectName(u"lblPassword")
        self.lblPassword.setGeometry(QRect(50, 140, 81, 16))
        self.lblPassword.setFont(font3)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Login", None))
        self.lblAdministrator.setText(QCoreApplication.translate("Widget", u"Administrator", None))
        self.lblLogin.setText(QCoreApplication.translate("Widget", u"Login", None))
        self.btnLogin.setText(QCoreApplication.translate("Widget", u"Login", None))
        self.lblUsername.setText(QCoreApplication.translate("Widget", u"Username", None))
        self.txtPassword.setText(QCoreApplication.translate("Widget", u"Password", None))
        self.lblPassword.setText(QCoreApplication.translate("Widget", u"Password", None))
    # retranslateUi

