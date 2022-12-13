import sys,os
sys.path.append(os.path.abspath(os.path.join(os.getcwd()+"/Game")))
import json
import random

SHAPE = 0
NUM = 1

class Card:
    damage = 1

    damage_map = {
        'colored': 10,
        'black': 7,
        'A': 3,
        '2': 2
    }

    def getDamage(self,card):
        return self.damage_map.get(card[NUM], 0)

    def isAttackCard(self, card):
        """
        Args:
            card `tuple`
            
        Return:
            Whether the card is an attack card or not
        """
        return card[SHAPE] == 'Joker' or card[NUM] in ['A', '2']

    

    @staticmethod
    def getCardImage(card):
        """
        Args:
            card `JSon` or `tuple`: Type of card
        Return:
         `str`: Image address 

        """

        if type(card) == list or type(card) == tuple:
            dict_card = {}
            dict_card['card_type'] = card[0]
            dict_card['number'] = card[1]

            card = dict_card

        if type(card) == str:
            card = json.loads(card)
        
            
        card_type = {'♥': 'hearts', '♣': 'clubs', '♠': 'spades', '◆': 'diamonds', 'Joker': 'Joker'}
        number = {}

        for i in range(2, 11):
            number[str(i)] = str(i)
        for char in 'AJQK':
            number[char] = char
        number['black'] = 'Black'
        number['colored'] = 'Color'

        

        return "PNG-cards-1.3/{0}{1}.png" .format(card_type[card['card_type']], number[card['number']])
        
    @staticmethod
    def cardToJson(card):
        """
        Args:
            card `Tuple`: Type of card
        Return:
            Json -> Type of card 
        """
        data = {'card_type': card[0], 'number': card[1]}
        return json.dumps(data)

    @staticmethod
    def makeDeck():
        # variable initialization
        deck = []
        shapes = '♥♣♠◆'
        nums = []

        for i in range(2, 11):
            nums.append(str(i))
        for c in 'JQKA':
            nums.append(c)

        # make deck(card)
        for shape in shapes:
            for num in nums:
                deck.append((shape, num))
                
        deck.append(('Joker', 'black'))
        deck.append(('Joker', 'colored'))

        deck = Card.shffleDeck(deck)

        return deck
        
    @staticmethod
    def shffleDeck(deck):
        random.shuffle(deck)
        return deck




