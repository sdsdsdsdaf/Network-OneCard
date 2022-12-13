import sys,os, json
sys.path.append(os.path.abspath(os.path.join(os.getcwd()+"/Game")))
from Card import Card

BASIC_GET_CARD_NUM = 7
SHAPE = 0
NUM = 1

class Room:
    """
    __init__(None)

    instance var :
        user_list `list`: list of `Dic`{user_socket, addr}
        chat_log `list`: Chatting log
        user_nickname_list `list`: list of use's NickName
        played_card `list`: Set of Paid Card
        last_card `Str`: Card
        deck `list`: Basic Card Deck

    Method:
        createRoom(self,user_data, nickname)

        appendPlayer(self, user_list)

    """
    user_list = []
    chat_log = []
    user_nickname_list = []
    played_card = []
    last_card = []
    deck = []
    turn = 1
    is_attack = False
    turn_table = {}

    def createRoom(self):

        self.deck.extend(Card.makeDeck())
        
        card = self.deck[-1]
        while card[SHAPE] == 'Joker':
            self.deck = Card.shffleDeck(self.deck)
        self.last_card = self.deck.pop()
        self.is_attack = False
        self.played_card = []

    def dataToJson(self):

        card_data = {
            'played_card': self.played_card,
            'last_card': self.last_card,
            'deck': self.deck,
            'is_attack': self.is_attack,
            'turn' : self.turn,
            'turn_table': self.turn_table
            }

        return json.dumps(card_data)

    def modifyFieldByJson(self, data):

        card_data = json.loads(data)

        self.played_card = card_data['played_card']
        self.last_card = card_data['last_card']
        self.deck = card_data['deck']
        self.is_attack = card_data['is_attack']
        self.turn = card_data['turn']
        self.turn_table = card_data['turn_table']

    def sendDataToUser(self, client_socket):
        data = self.dataToJson()
        data = data.encode()
        client_socket.sendall(data)
        print("%d바이트 데이터 전송 완료" %sys.getsizeof(self.dataToJson())+ self.dataToJson())


    def appendPlayer(self, user_list):
        """
        Args:
            ({'user_socket': client_socket, 'addr': addr}, nickname, my_id)

            user_list `list`:  list of user's information `Tuple`
            ( `Dic` {user_socket, addr}, `str` User Nickname)

        Return:
            None -> modify Room`s instance var user_list
        """
        for user_data in user_list:
            self.user_list.append(user_data[0])
            self.user_nickname_list.append(user_data[1])
            self.turn_table[user_data[2]] = len(self.turn_table) + 1

            print(len(self.turn_table), self.turn_table)

            if len(user_list) >= 4:
                self.turn = 1

    def deletePlayer(self, user_list):

        for user_data in user_list:
            
            self.user_list.remove(user_data[0])
            self.user_nickname_list.remove(user_data[1])
            turn = self.turn_table.pop(user_data[2])

            for key, value in self.turn_table.items():
                if turn < value:
                    self.turn_table[key] = value - 1

            
    def deletePlayer(self, user_list, id):
        """
        Args:
            user_list `list`:  list of user's information `Tuple`
            ( `Dic` {user_socket, addr}, `str` User Nickname)

        Return:
            None -> modify Room`s instance var user_list
        """

        for user_data in user_list:
            self.user_list.remove(user_data[0])
            self.user_nickname_list.remove(user_data[1])
            self.turn_table.pop(id)

if __name__ == "__main__":
    room1 = Room()
    room1.createRoom(user_data={'user_socket': 12133, 'addr':'12'}, nickname= 'hi')
    print(room1.deck)
    print("Len: ", len(room1.deck))
    print("Last_card: ", room1.last_card)
