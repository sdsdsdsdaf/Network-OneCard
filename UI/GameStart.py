# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GameStartWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd())))
sys.path.append(os.path.abspath(os.path.join(os.getcwd() + "/UI")))

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout, QMainWindow
from PyQt5.QtWidgets import QWidget, QDesktopWidget
from exitUI import Ui_Exit
from ButtonStyle import ButtonStyle

class StartWindow(QMainWindow, QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__() #super 명시적으로 불러오기
        self.setupUi()
        self.center()

    def setupUi(self):
        self.setObjectName("OneCard")
        self.setFixedSize(1089, 820)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("PNG-cards-1.3/blackjack.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color:rgb(45, 156, 15);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 170, 851, 111))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("PNG-cards-1.3/title.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(-1)
        self.label.setObjectName("title")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 390, 491, 91))
        self.pushButton.setStyleSheet("background-color: rgb(230, 230, 114)")
        self.pushButton.setObjectName("Start")
        self.pushButton.clicked.connect(self._gameStart)
        ButtonStyle.setButtonStyle(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 530, 491, 91))
        self.pushButton_2.setStyleSheet("background-color: rgb(230, 230, 114)")
        self.pushButton_2.setObjectName("Exit")
        ButtonStyle.setButtonStyle(self.pushButton_2)
        

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.grid = QGridLayout()
        self.grid.addWidget(self.label, 1, 1)
        self.grid.addWidget(self.pushButton, 2, 1)
        self.grid.addWidget(self.pushButton_2, 3, 1)
        
        self.pushButton_2.clicked.connect(self.__gameEnd)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, OneCard):
        _translate = QtCore.QCoreApplication.translate
        OneCard.setWindowTitle(_translate("OneCard", "One card"))
        self.pushButton.setText(_translate("OneCard", "Game Start"))
        self.pushButton_2.setText(_translate("OneCard", "Exit"))

    def _gameStart(self):
        self.switch_window.emit()

    def __gameEnd(self):
        exitWindow = QtWidgets.QDialog()
        exit = Ui_Exit()
        exit.setupUi(exitWindow)
        exitWindow.show()
        exitWindow.exec_()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

#import BackGround_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    onecard = StartWindow()
    onecard.show()
    sys.exit(app.exec_())

