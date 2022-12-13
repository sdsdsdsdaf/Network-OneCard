import sys,os
sys.path.append(os.path.abspath(os.path.join(os.getcwd() + "/Game")))

import socket
from threading import Thread
from Room import Room

import threading
lock = threading.Lock()

class Server:

    IP = "127.0.0.1"
    port = 9999
    server_socket = None
    id = 0

    def __init__(self):
        self.setIPPort()

    def setIPPort(self, ip = '127.0.0.1', port = 9999):
        self.IP = ip
        self.port = port

    def getIPPort(self):

        """
        return `Dic`: 
            {'Host_IP': self.IP, 'Port': self.port}
        """
        return {'Host_IP': self.IP, 'Port': self.port}

    def handle_receive(self, client_socket, addr, room):

        lock.acquire(blocking=True, timeout=-1)#Sys

        self.id+=1
        my_id = self.id
        print(self.id)
 
        #nickname input
        data = client_socket.recv(1024)
        nickname = data.decode()
        print("NickName: ", nickname)
        room.appendPlayer([({'user_socket': client_socket, 'addr': addr}, nickname, my_id)])

        #send inital Condition
        client_socket.sendall(str(my_id).encode())

        if str(my_id) != client_socket.recv(1024).decode():
            print("Not Correct Id")
            sys.exit()

        room.sendDataToUser(client_socket)
        
        

        #Initalize
        json_data = client_socket.recv(2048)
        json_data = json_data.decode()
        room.modifyFieldByJson(json_data)

        for con in room.user_list:
            try:
                room.sendDataToUser(con['user_socket'])
            except:
                print("연결이 비 정상적으로 종료된 소켓 발견")
        
        lock.release()

        while True:
            data = client_socket.recv(2048)
            data = data.decode()
            

            if data == 'end the game!':
                break
            else:
                room.modifyFieldByJson(data)
                for con in room.user_list:
                    try:
                        room.sendDatatoUser(con['user_socket'])

                    except:
                        print("연결이 비 정상적으로 종료된 소켓 발견")

            i+=1
        #delete User Information
        room.deletePlayer([({'user_socket': client_socket, 'addr': addr}, nickname, my_id)])
        client_socket.close()

    def openServer(self):
        
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.IP, self.port))
        self.server_socket.listen(5)
        print("Open Server")
        room1 = Room()
        room1.createRoom()

        while True:

            client_socket, addr = self.server_socket.accept()
            print("클라이언트 연결")
            event_th = Thread(target= self.handle_receive, args=(client_socket, addr, room1))
            event_th.start()

    
    def closeServer(self):
        self.server_socket.close()
        print("Close server")

if __name__ == "__main__":
    server1 = Server()
    server1.openServer()