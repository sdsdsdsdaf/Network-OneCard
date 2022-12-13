import sys,os
sys.path.append(os.path.abspath(os.path.join(os.getcwd()+"/Game")))

from Card import Card
import random
import json
import socket

SHAPE = 0
NUM = 1

class User(Card):

    user_socket = None
    user_addr = None
    nickname = None
    played_card = None
    last_card = None
    deck = None
    is_attack = False
    turn = None
    turn_table = None
    __hand = []
    my_id = None

    def __init__(self, user_socket, user_addr, nickname):
        """
        Args:
            num `int`: How many cards do you get at first
            played_card `list`: already paid card
            deck `list`: The set of card
            user_socket `Socket` : user's socket
            user_addr `Tcp address` : Tcp address
            nickName `str`: nickname

        """
        super().__init__()
        self.__hand = []
        self.user_socket = user_socket
        self.user_addr = user_addr
        self.nickname = nickname

    def getInitDataFromServer(self, num):
        
        #id 받기
        data = self.user_socket.recv(1024)
        self.my_id = data.decode()

        print("id: "+self.my_id, type(self.my_id))

        #id 확인 메세지 전송
        self.user_socket.sendall(self.my_id.encode())

        self.getDataFromServer()
        
        self.getCardInDeck(num)

    def getHand(self):
        return self.__hand
        
    def getDataFromServer(self):
        
        """
        Data Format:

            'played_card': self.played_card,
            'last_card': self.last_card,
            'deck': self.deck,
            'is_attack': self.is_attack,
            'turn' : self.turn
            'turn_table': self.turn_table
        
        """

        data = self.user_socket.recv(2048)
        json_data = data.decode()
        data = json.loads(json_data)

        self.played_card = data['played_card']
        self.deck = data['deck']
        self.is_attack = data['is_attack']
        self.last_card = data['last_card']
        self.turn = data['turn']
        self.turn_table = data['turn_table']

        return data

    def sendNickname(self):
        send_data = self.nickname
        send_data = send_data.encode()
        self.user_socket.sendall(send_data)

    def sendDatatoServer(self):

        send_data = {}
        send_data['played_card'] = self.played_card
        send_data['last_card'] = self.last_card
        send_data['deck'] = self.deck
        send_data['is_attack'] = self.is_attack
        send_data['turn'] = self.turn
        send_data['turn_table'] = self.turn_table

        send_data = json.dumps(send_data)
        send_data = send_data.encode()
        self.user_socket.sendall(send_data)

    def getAvailableCardSet(self):
        """
        Args:
            last_card `tuple`: What is the The last card user paid

        Return:
            The set of available card
        """
        available = []

        if not self.is_attack and self.last_card[NUM] == 'Joker':
            color_or_black = {'colored': ['♥','◆'], 'black': ['♣', '♠']}

            for card in self.__hand:
                if card[SHAPE] in color_or_black[self.last_card[SHAPE]]:
                    available.append(card)
            
            return available

        for card in self.__hand:

            if card[SHAPE] == 'Joker':
                if card[NUM] == 'colored' and(self.last_card[SHAPE] == '♥' or self.last_card[SHAPE] == '◆'):
                    available.append(card)
                if card[NUM] == 'black' and(self.last_card[SHAPE] == '♣' or self.last_card[SHAPE] == '♠'):
                    available.append(card)
                
            elif card[SHAPE] != self.last_card[SHAPE] and card[NUM] != self.last_card[NUM]:
                continue
            elif self.is_attack:
                # Append the stronger or same number card
                if self.getDamage(card) >= self.getDamage(self.last_card):
                    available.append(card)
                # Append defensive card
                elif (card[SHAPE] == self.last_card[SHAPE] and card[NUM] == '3' and self.last_card[NUM] == '2'):
                    available.append(card)

            else:
                available.append(card)

        return available

    def draw(self):

        """
        Args:
            played_card `list`: already paid card
            deck `list`: The set of card

        Return:
            result `tuple`
        """

        self.__hand.append(self.deck.pop())

        if len(self.deck) == 0:
            print("카드를 다시 섞습니다!")
            last_card = self.played_card.pop()
            random.shuffle(self.played_card)
            self.played_card, self.deck = self.deck, self.played_card
            self.played_card.append(last_card)

    def getCardInDeck(self, number):

        """
        Args:
            number `int`: The number of a card to import 
            played_card `list`: already paid card
            deck `list`: The set of card

        Return:
            None -> modify hand, played_card, deck
        """

        for _ in range(number):
            self.draw()
        

    def betCard(self, index):
        """
        Args:
            index `int`: The index of chosen
            played_card `list`: already paid card

        Return:
            None -> modify hand, played_card, deck
        """
        self.played_card.append(self.__hand.pop(index))

    def isMyTurn(self):
        print(self.turn, self.turn_table[self.my_id])
        return self.turn == self.turn_table[self.my_id]

if __name__ == "__main__":
    deck = Card.makeDeck()
    played_list = []
    print(len(deck))

    user1 = User(7, played_list, deck, "av")
    user1.getCardInDeck(2, played_list, deck)
    print(user1.getHand())

    user1.betCard(0, played_list)
    print(played_list)
    print(len(deck), len(played_list))
