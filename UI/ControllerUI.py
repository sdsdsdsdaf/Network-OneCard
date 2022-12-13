import sys
import os
from time import sleep
from threading import Thread
sys.path.append(os.path.abspath(os.path.join(os.getcwd())))

from UI.GameStart import StartWindow
from UI.WatingRoom import Ui_Onecard
from PyQt5.QtWidgets import QApplication
from Game.User import User
from UI.MainGameUi import MainGameUi
from PyQt5 import QtCore, QtGui, QtWidgets
from Game.Card import Card
# from MainGameGui import 

BASIC_GET_CARD_NUM = 7

class Notification:

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(277, 124)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 0, 221, 111))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Wating other User"))
        




class NicknameInputWindow:
    
    nick = None
    controller = None


    def __init__(self, input_window, controller_obj) -> None:
        self.input_window = input_window
        self.controller = controller_obj

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

    def waitOtherPlayer(self , di):

        print("쓰레드 시작")

        turn_table = {}
        while len(turn_table) < 2:#4

            turn_table = self.controller.user_obj.getDataFromServer()['turn_table']
            print(len(turn_table))
            print(turn_table)

        print("쓰레드 끝")
        di.close()

    
    def btnCmd(self):

        self.nick = self.lineEdit.text()
        self.input_window.close()
        
        self.controller.user_obj = User(self.controller.client_socket, self.controller.user_addr, self.nick)
        
        print("Sending Nickname")
        self.controller.user_obj.sendNickname()
        print("Send complete")

        self.controller.user_obj.getInitDataFromServer(BASIC_GET_CARD_NUM)

        self.controller.user_obj.sendDatatoServer()
        print(self.nick)
        self.controller.user_obj.id = id

        Dialog = QtWidgets.QDialog()
        ui = Notification()
        ui.setupUi(Dialog)
        Dialog.show()


        #싱크로
        
        th1 = Thread(target = self.waitOtherPlayer, args=tuple([Dialog]))
    
        th1.start()
        Dialog.exec_()

        th1.join()
        print("join 완료")


        Dialog = QtWidgets.QDialog()
        ui = Notification()
        ui.setupUi(Dialog)
        ui.label.setText(QtCore.QCoreApplication.translate("Dialog", "Game Start"))
        Dialog.show()

        #played_card, user_hand card inital
        def exit(obj, Dialog_obj):
            obj.controller.reloadImage()
            print(obj.controller.user_obj.getHand())
            obj.controller.main_game_window.select_card_view.setPixmap(QtGui.QPixmap(Card.getCardImage(obj.controller.user_obj.getHand()[0])))
            obj.controller.main_game_window.select_card_view.repaint()

            sleep(1)
            Dialog_obj.close()

        th1 = Thread(target = exit, args=(self, Dialog))
        th1.start()
        Dialog.exec_()
        


        print("Game Start")


    def retranslateUi(self, InputWindow):
        _translate = QtCore.QCoreApplication.translate
        InputWindow.setWindowTitle(_translate("InputWindow", "NickName"))
        self.pushButton.setText(_translate("InputWindow", "확인"))
        self.label.setText(_translate("InputWindow", "Enter Your Nick Name"))

class MyController:

    user_obj = None
    user_addr = None
    client_socket = None

    def __init__(self, client_socket, user_addr):

        self.setClientSocketAndAddr(client_socket, user_addr)

        self.first_window = StartWindow()
        self.WatingRoomWindow = Ui_Onecard()
        self.main_game_window = MainGameUi()
        self.first_window.show()
        self.first_window.switch_window.connect(lambda:[self.startGame(self.main_game_window)])
        self.WatingRoomWindow.switch_window.connect(lambda:[self.showWindow(self.first_window)])
        self.main_game_window.right_select_event.connect(self.selectRight)
        self.main_game_window.left_select_event.connect(self.selectLeft)
        self.main_game_window.select_event.connect(self.select)
        
        
        MyController.windowlist = [self.first_window, self.WatingRoomWindow, self.main_game_window]

    def setClientSocketAndAddr(self, client_socket, user_addr):
        self.client_socket = client_socket
        self.user_addr = user_addr

    def startGame(self, showing_window):

        InputWindow = QtWidgets.QDialog()
        input = NicknameInputWindow(InputWindow, self)
        input.setupUi(InputWindow)
        nick = input.nick
        print(nick)

        InputWindow.show()
        InputWindow.exec_()
        self.showWindow(showing_window)


    def showWindow(self, showing_window):
        MyController.windowlist

        for window in MyController.windowlist:
            if window == showing_window:
                window.show()
            else:
                window.hide()
    
    def selectRight(self):
        if self.main_game_window.selected_card >= len(self.user_obj.getHand()):
            self.main_game_window.selected_card = 0
            return

        self.main_game_window.select_card_view.setPixmap(QtGui.QPixmap(Card.getCardImage(self.user_obj.getHand()[self.main_game_window.selected_card])))
        self.main_game_window.select_card_view.repaint()
        
    def selectLeft(self):
        if self.main_game_window.selected_card < 0:
            self.main_game_window.selected_card = len(self.user_obj.getHand()) - 1
            return

        self.main_game_window.select_card_view.setPixmap(QtGui.QPixmap(Card.getCardImage(self.user_obj.getHand()[self.main_game_window.selected_card])))
        self.main_game_window.select_card_view.repaint()
    

    def select(self): 

        if not self.user_obj.isMyTurn():
            print("Not your turn")
            Dialog = QtWidgets.QDialog()
            ui = Notification()
            ui.setupUi(Dialog)
            ui.label.setText(QtCore.QCoreApplication.translate("Dialog","Not Your Turn"))
            Dialog.show()
            Dialog.exec_()
            return

        available_card = self.user_obj.getAvailableCardSet()
        print("available_card", available_card)

        if not self.user_obj.getHand()[self.main_game_window.selected_card] in available_card:
            print("Not available Card", self.user_obj.getHand()[self.main_game_window.selected_card])
            Dialog = QtWidgets.QDialog()
            ui = Notification()
            ui.setupUi(Dialog)
            ui.label.setText(QtCore.QCoreApplication.translate("Dialog","Not Available Card!!"))
            Dialog.show()
            Dialog.exec_()
            return 
        
        self.user_obj.betCard(self.main_game_window.selected_card, self.user_obj.played_card)
        self.turn %= 4
        self.turn += 1
        self.user_obj.sendDatatoServer()
        self.user_obj.getDataFromServer()
        self.reloadImage()

    def reloadImage(self):
        

        
        self.main_game_window.hand_cards.clear()

        for hand_card in self.user_obj.getHand():
            print(hand_card)

            hand_card = QtWidgets.QLabel(self.main_game_window.centralwidget)
            hand_card.setGeometry(QtCore.QRect(self.main_game_window.hand_cards_x[-1], 470, 81, 121))
            self.main_game_window.hand_cards_x.append(self.main_game_window.hand_cards_x[-1] + 40)

            hand_card.setText("")
            hand_card.setPixmap(QtGui.QPixmap("PNG-cards-1.3/background.png"))
            hand_card.setObjectName("hand_card")
            self.main_game_window.hand_cards.append(hand_card)
            
        
        self.main_game_window.last_card.setPixmap(QtGui.QPixmap(Card.getCardImage(self.user_obj.last_card)))
        self.main_game_window.last_card.repaint()

    def playMainGame(self):

        if self.user_obj.isMyTurn():
                if len(self.user_obj.getAvailableCardSet()) == 0 and not self.user_obj.is_attack:
                    self.draw()
                    self.turn %= 4
                    self.turn += 1
                    self.user_obj.sendDatatoServer()
                    self.user_obj.getDataFromServer()
                    
                if len(self.user_obj.getAvailableCardSet()) == 0 and self.user_obj.is_attack:
                    for _ in range(self.getDamage(self.last_card)):
                        self.draw()
                        self.turn %= len(self.user_obj.turn_table)
                        self.turn += 1
                        self.user_obj.sendDatatoServer()
                        self.user_obj.getDaraFromServer()
                    

        

        while True:
            try:
                self.user_obj.getDataFromServer()
            except:
                print("연결 끊김")
            self.reloadImage()

            if self.user_obj.isMyTurn():
                if len(self.user_obj.available_card()) == 0 and not self.user_obj.is_attack:
                    self.draw()
                    self.turn %= 4
                    self.turn += 1
                    self.user_obj.sendDatatoServer()
                    self.user_obj.getDataFromServer()
                if len(self.user_obj.available_card()) == 0 and self.user_obj.is_attack:
                    for _ in range(self.getDamage(self.last_card)):
                        self.draw()
                        self.turn %= 4
                        self.turn += 1
                        self.user_obj.sendDatatoServer()
                        self.user_obj.getDataFromServer()

                # 종료 조건
                if len(self.user_obj.getHand()) > 16:
                    self.user_obj.user_socket.sendall("end the game!".encode())

        

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    controller = MyController(0,0)
    controller.setClientSocketAndAddr(123,123) # QDialog 나 QMainWindow 상속받고 __init__에 setUI불러서 실해시켜버리기
    sys.exit(app.exec_())
    