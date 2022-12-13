# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WatingRoomWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.getcwd()+"/UI")))

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QDialog
from ButtonStyle import ButtonStyle

class Ui_Onecard(QDialog, QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("self")
        self.resize(1089, 820)
        self.setStyleSheet("background-color:rgb(45, 156, 15);")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(492, 517, 171, 41))
        self.pushButton.setStyleSheet("background-color: rgb(230, 230, 114)\n")
        self.pushButton.setObjectName("pushButton")
        self.WatingRoomList = QtWidgets.QGroupBox(self)
        self.WatingRoomList.setGeometry(QtCore.QRect(30, 50, 641, 381))
        self.WatingRoomList.setObjectName("WatingRoomList")
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.pushButton.clicked.connect(self.switch_window.emit)
        ButtonStyle.setButtonStyle(pushButton=self.pushButton, size= 15)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "One Card"))
        self.pushButton.setText(_translate("self", "Back to Main"))
        self.WatingRoomList.setTitle(_translate("self", "WatingRoomList"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    self = Ui_Onecard()
    self.show()
    sys.exit(app.exec_())

