# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exit.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.getcwd()+"/UI")))

class Ui_Exit(object):
    Exit =None

    def setupUi(self, Exit):

        self.Exit = Exit

        Exit.setObjectName("Exit")
        Exit.resize(373, 103)
        self.Qlabel = QtWidgets.QLabel(Exit)
        self.Qlabel.setGeometry(QtCore.QRect(120, 10, 161, 31))
        self.Qlabel.setObjectName("Qlabel")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Exit)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 321, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.yesButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.yesButton.setObjectName("yesButton")
        self.horizontalLayout.addWidget(self.yesButton)
        self.noButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.noButton.setObjectName("noButton")
        self.horizontalLayout.addWidget(self.noButton)

        self.retranslateUi(Exit)
        QtCore.QMetaObject.connectSlotsByName(Exit)

        self.noButton.clicked.connect(self.closeCloseWindow)
        self.yesButton.clicked.connect(self.gameEnd)

    def closeCloseWindow(self):
        self.Exit.close()
        

    def gameEnd(self):
        QtCore.QCoreApplication.instance().quit()

    def retranslateUi(self, Exit):
        _translate = QtCore.QCoreApplication.translate
        Exit.setWindowTitle(_translate("Exit", "Exit"))
        self.Qlabel.setText(_translate("Exit", "Are you sure exit?"))
        self.yesButton.setText(_translate("Exit", "Yes"))
        self.noButton.setText(_translate("Exit", "No"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Exit = QtWidgets.QDialog()
    ui = Ui_Exit()
    ui.setupUi(Exit)
    Exit.show()
    sys.exit(app.exec_())

