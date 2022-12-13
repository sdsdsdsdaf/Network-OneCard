# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NickName.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InputWindow(object):

    def __init__(self, InputWindow) -> None:
        self.setupUi(InputWindow)
        InputWindow.show()

    def setupUi(self, InputWindow):
        InputWindow.setObjectName("InputWindow")
        InputWindow.resize(400, 106)
        self.pushButton = QtWidgets.QPushButton(InputWindow)
        self.pushButton.setGeometry(QtCore.QRect(290, 40, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:[self.btnCmd()])

        self.label = QtWidgets.QLabel(InputWindow)
        self.label.setGeometry(QtCore.QRect(60, 10, 151, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(InputWindow)
        self.lineEdit.setGeometry(QtCore.QRect(40, 40, 181, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(InputWindow)
        QtCore.QMetaObject.connectSlotsByName(InputWindow)

    def retranslateUi(self, InputWindow):
        _translate = QtCore.QCoreApplication.translate
        InputWindow.setWindowTitle(_translate("InputWindow", "NickName"))
        self.pushButton.setText(_translate("InputWindow", "확인"))
        self.label.setText(_translate("InputWindow", "Enter Your Nick Name"))
    
    def btnCmd(self):
        text = self.lineEdit.text()
        print(text)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InputWindow = QtWidgets.QDialog()
    Ui_InputWindow(InputWindow)
    sys.exit(app.exec_())

