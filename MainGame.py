from UI.ControllerUI import MyController
import sys
import socket
from PyQt5.QtWidgets import QApplication

class MainGame:

    __Host = None
    __Port = None
    controller = None

    def __init__(self):
        self.setHostPort()
        result = self.connectServer()
        self.controller = MyController(result[0], result[1])
    
    def setHostPort(self, Host = '127.0.0.1', Port = 9999):
        self.__Host = Host
        self.__Port = Port

    def getHostPort(self):

        """
        return `Dic`: 
            {'Host_IP': self.__Host, 'Port': self.__port}
        """

        return {'Host_IP': self.__Host, 'Port': self.__Port}

    def connectServer(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.__Host, self.__Port))

        return client_socket,0
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game1 = MainGame()
    sys.exit(app.exec_())