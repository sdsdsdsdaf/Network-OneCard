# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Maingame.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ButtonStyle import ButtonStyle
from PyQt5.QtWidgets import QWidget, QMainWindow

class MainGameUi(QMainWindow, QWidget):

    left_select_event = QtCore.pyqtSignal()
    right_select_event = QtCore.pyqtSignal()
    select_event = QtCore.pyqtSignal()
    hand_cards = []
    hand_cards_x = [100]
    selected_card = 0
    select_card_view = None

    def __init__(self):
        super().__init__() #super 명시적으로  불러오기
        self.setupUi()

    def setupUi(self):

        self.setObjectName("MainGameUi")
        self.setFixedSize(1089, 820)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("PNG-cards-1.3/blackjack.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color: rgb(45, 156, 15);")

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.last_card = QtWidgets.QLabel(self.centralwidget)
        self.last_card.setGeometry(QtCore.QRect(480, 250, 81, 121))
        self.last_card.setText("")
        self.last_card.setPixmap(QtGui.QPixmap("PNG-cards-1.3/background.png"))
        self.last_card.setObjectName("last_card")

        self.otherplayer3_4 = QtWidgets.QLabel(self.centralwidget)
        self.otherplayer3_4.setGeometry(QtCore.QRect(1010, 320, 81, 80))
        self.otherplayer3_4.setText("")
        self.otherplayer3_4.setPixmap(QtGui.QPixmap("PNG-cards-1.3/background90.png"))
        self.otherplayer3_4.setObjectName("otherplayer3_4")

        self.otherplayer3_1 = QtWidgets.QLabel(self.centralwidget)
        self.otherplayer3_1.setGeometry(QtCore.QRect(1010, 200, 81, 80))
        self.otherplayer3_1.setText("")
        self.otherplayer3_1.setPixmap(QtGui.QPixmap("PNG-cards-1.3/background90.png"))
        self.otherplayer3_1.setObjectName("otherplayer3_1")

        self.otherplayer3_2 = QtWidgets.QLabel(self.centralwidget)
        self.otherplayer3_2.setGeometry(QtCore.QRect(1010, 240, 81, 80))
        self.otherplayer3_2.setText("")
        self.otherplayer3_2.setPixmap(QtGui.QPixmap("PNG-cards-1.3/background90.png"))
        self.otherplayer3_2.setObjectName("otherplayer3_2")

        self.otherplayer3_5 = QtWidgets.QLabel(self.centralwidget)
        self.otherplayer3_5.setGeometry(QtCore.QRect(1010, 360, 81, 80))
        self.otherplayer3_5.setText("")
        self.otherplayer3_5.setPixmap(QtGui.QPixmap("PNG-cards-1.3/background90.png"))
        self.otherplayer3_5.setObjectName("otherplayer3_5")

        self.labotherplayer3_3 = QtWidgets.QLabel(self.centralwidget)
        self.labotherplayer3_3.setGeometry(QtCore.QRect(1010, 280, 81, 80))
        self.labotherplayer3_3.setText("")
        self.labotherplayer3_3.setPixmap(QtGui.QPixmap("PNG-cards-1.3/background90.png"))
        self.labotherplayer3_3.setObjectName("labotherplayer3_3")

        self.otherplayer1_1 = QtWidgets.QLabel(self.centralwidget)
        self.otherplayer1_1.setGeometry(QtCore.QRect(-30, 360, 121, 80))
        self.otherplayer1_1.setText("")
        self.otherplayer1_1.setPixmap(QtGui.QPixmap("PNG-cards-1.3/background90.png"))
        self.otherplayer1_1.setObjectName("otherplayer1_1")

        self.otherplayer1_2 = QtWidgets.QLabel(self.centralwidget)
        self.otherplayer1_2.setGeometry(QtCore.QRect(-30, 320, 121, 80))
        self.otherplayer1_2.setText("")
        self.otherplayer1_2.setPixmap(QtGui.QPixmap("PNG-cards-1.3/background90.png"))
        self.otherplayer1_2.setObjectName("otherplayer1_2")

        self.otherplayer1_3 = QtWidgets.QLabel(self.centralwidget)
        self.otherplayer1_3.setGeometry(QtCore.QRect(-30, 280, 121, 80))
        self.otherplayer1_3.setText("")
        self.otherplayer1_3.setPixmap(QtGui.QPixmap("PNG-cards-1.3/background90.png"))
        self.otherplayer1_3.setObjectName("otherplayer1_3")

        self.otherplayer1_4 = QtWidgets.QLabel(self.centralwidget)
        self.otherplayer1_4.setGeometry(QtCore.QRect(-30, 240, 121, 80))
        self.otherplayer1_4.setText("")
        self.otherplayer1_4.setPixmap(QtGui.QPixmap("PNG-cards-1.3/background90.png"))
        self.otherplayer1_4.setObjectName("otherplayer1_4")

        self.otherplayer1_5 = QtWidgets.QLabel(self.centralwidget)
        self.otherplayer1_5.setGeometry(QtCore.QRect(-30, 200, 121, 80))
        self.otherplayer1_5.setText("")
        self.otherplayer1_5.setPixmap(QtGui.QPixmap("PNG-cards-1.3/background90.png"))
        self.otherplayer1_5.setObjectName("otherplayer1_5")

        self.otherplayer2_1 = QtWidgets.QLabel(self.centralwidget)
        self.otherplayer2_1.setGeometry(QtCore.QRect(410, -20, 80, 121))
        self.otherplayer2_1.setText("")
        self.otherplayer2_1.setPixmap(QtGui.QPixmap("PNG-cards-1.3/background.png"))
        self.otherplayer2_1.setObjectName("otherplayer2_1")

        self.otherplayer2_2 = QtWidgets.QLabel(self.centralwidget)
        self.otherplayer2_2.setGeometry(QtCore.QRect(450, -20, 80, 121))
        self.otherplayer2_2.setText("")
        self.otherplayer2_2.setPixmap(QtGui.QPixmap("PNG-cards-1.3/background.png"))
        self.otherplayer2_2.setObjectName("otherplayer2_2")

        self.otherplayer2_3 = QtWidgets.QLabel(self.centralwidget)
        self.otherplayer2_3.setGeometry(QtCore.QRect(490, -20, 80, 121))
        self.otherplayer2_3.setText("")
        self.otherplayer2_3.setPixmap(QtGui.QPixmap("PNG-cards-1.3/background.png"))
        self.otherplayer2_3.setObjectName("otherplayer2_3")

        self.otherplayer2_4 = QtWidgets.QLabel(self.centralwidget)
        self.otherplayer2_4.setGeometry(QtCore.QRect(530, -20, 80, 121))
        self.otherplayer2_4.setText("")
        self.otherplayer2_4.setPixmap(QtGui.QPixmap("PNG-cards-1.3/background.png"))
        self.otherplayer2_4.setObjectName("otherplayer2_4")

        self.otherplayer2_5 = QtWidgets.QLabel(self.centralwidget)
        self.otherplayer2_5.setGeometry(QtCore.QRect(570, -20, 80, 121))
        self.otherplayer2_5.setText("")
        self.otherplayer2_5.setPixmap(QtGui.QPixmap("PNG-cards-1.3/background.png"))
        self.otherplayer2_5.setObjectName("otherplayer2_5")

        self.select_card_view = QtWidgets.QLabel(self.centralwidget)
        self.select_card_view.setGeometry(QtCore.QRect(950, 650, 81, 121))
        self.select_card_view.setText("")
        self.select_card_view.setPixmap(QtGui.QPixmap(""))
        self.select_card_view.setObjectName("hand_card")

        self.left_select = QtWidgets.QPushButton(self.centralwidget)
        self.left_select.setGeometry(QtCore.QRect(200, 680, 141, 91))
        self.left_select.setObjectName("left_select")
        ButtonStyle.setButtonStyle(self.left_select)
        self.left_select.clicked.connect(self.left_select_push)

        self.right_select = QtWidgets.QPushButton(self.centralwidget)
        self.right_select.setGeometry(QtCore.QRect(720, 680, 141, 91))
        self.right_select.setObjectName("right_select")
        ButtonStyle.setButtonStyle(self.right_select)
        self.right_select.clicked.connect(self.right_select_push)

        self.select = QtWidgets.QPushButton(self.centralwidget)
        self.select.setGeometry(QtCore.QRect(460, 680, 141, 91))
        self.select.setObjectName("selcet")
        ButtonStyle.setButtonStyle(self.select)
        self.select.clicked.connect(self.select_push)
        

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")

        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def hover(self, index):
        self.hand_cards[index].move(self.hand_cards_x[index], 510)

    def down(self, index):
        winPos=self.hand_cards[index].pos() 
        globalWinPos = self.mapToGlobal(winPos) 
        self.hand_cards[index].move(globalWinPos.x, globalWinPos.y - 40)
        self.hand_cards[index].repaint()

    def generateHandCards(self):

        for _ in range(17):

            hand_card = QtWidgets.QLabel(self.centralwidget)
            hand_card.setGeometry(QtCore.QRect(self.hand_cards_x[-1], 470, 81, 121))
            self.hand_cards_x.append(self.hand_cards_x[-1] + 40)

            hand_card.setText("")
            hand_card.setPixmap(QtGui.QPixmap("PNG-cards-1.3/background.png"))
            hand_card.setObjectName("hand_card")
            self.hand_cards.append(hand_card)

        

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainGameUi", "One card"))
        self.left_select.setText(_translate("MainGameUi", "Left"))
        self.right_select.setText(_translate("MainGameUi", "Right"))
        self.select.setText(_translate("MainGameUi", "Select"))
        

    def right_select_push(self):
        self.right_select_event.emit()
        self.selected_card += 1
        print("Right Button Push")
    
    def left_select_push(self):
        self.selected_card -= 1
        self.left_select_event.emit()
        print("Left Button Push")

    def select_push(self):
        self.select_event.emit()
        print("Selclt Button Push")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainGameUi()
    ui.setupUi()
    ui.hover(1)
    ui.show()
    sys.exit(app.exec_())

