import socket
import os
from _thread import *
import threading
import random
import collections

# locking for synchronization of threads
lock = threading.Lock()

# variable initialization
deck = []
shapes = '♥♣♠◆'
nums = []
is_attack = False
damage = 1
put = []

# Get available card
def getAvailable(hand, last_card, is_attack):
    available = []

    # If the card on the table is joker
    if not is_attack and last_card[0] == 'Joker':
        available.extend(hand)
        return available

    for card in hand:
        if card[0] == 'Joker':
            available.append(card)

        elif (card[0] != last_card[0] and card[1] != last_card[1]):
            continue

        elif is_attack:
            # Append the stronger or same number card
            if get_damage(card) >= get_damage(last_card):
                available.append(card)
            # Append defensive card
            elif (card[0] == last_card[0] and card[1] == '3' and last_card[1] == '2'):
                available.append(card)

        else:
            available.append(card)

    return available


def is_attack_card(card):
    return card[0] == 'Joker' or card[1] in ['A', '2']

damage_map = {
    'colored': 10,
    'black': 7,
    'A': 3,
    '2': 2
}

def get_damage(card):
    global damage_map
    return damage_map.get(card[1], 0)

def draw(hand):
    global put, deck

    hand.append(deck.pop())

    if len(deck) == 0:
        print("카드를 다시 섞습니다!")
        last_card = put.pop()
        random.shuffle(put)
        put, deck = deck, put
        put.append(last_card)


def turn(person):
    # Global variable
    global put, deck, is_attack, damage
    name = person.name
    hand = person.hand

    # GUI(누구(person)의 차례인지 알려준다)

    # select one of available cards
    available = getAvailable(hand, put[-1], is_attack)
    selected = None
    is_available = len(available) > 0
    if is_available:
        while True:
            # Client, GUI(낼 수 있는 카드 중 플레이어가 선택한 카드의 index를 i에 저장)
            # receive command
            i = clientConnection.recv(1024).decode('utf-8')

            if not i.isdigit():
                # GUI(에러 -숫자를 입력해주세요)
                continue
            i = int(i) - 1
            if i >= len(available):
                # GUI(에러 -범위 내의 숫자를 입력해주세요)
                continue
            if i != -1:
                selected = available[i]
                # send response
                clientConnection.send(i.encode('utf-8'))
            break

    else:
        print()
        # GUI(플레이어가 낼 수 있는 카드가 없습니다)

    # Open the selected card
    if selected is not None:
        hand.remove(selected)
        put.append(selected)

        if is_attack_card(selected):
            if not is_attack:
                damage = get_damage(selected)
            else:
                damage += get_damage(selected)

            is_attack = True

        # Defensive card
        elif selected[1] == '3':
            is_attack = False
            damage = 1

    # Take cards
    else:
        is_attack = False
        for i in range(damage):
            draw(hand)
        damage = 1
        selected = '00'

    return selected[1]



if __name__ == "__main":
    IP = "127.0.0.1"
    port = 8800

    # open server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, port))
    server_socket.listen()
    print("Start server running")
    
    # Server incoming connections "one by one"
    count = 0
    while count != 5:
        (clientConnection, clientAddress) = server_socket.accept()
        count += 1
        print("Accepted {} connections so far".format(count))

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
        random.shuffle(deck)

        # make players and give 7 cards to each players
        Person = collections.namedtuple('Person', 'name hand')
        people = []

        for i in range(4):
            people.append(Person(f'Player{i+1}', []))

        for i in range(7):    
            people[0].hand.append(deck.pop())
            people[1].hand.append(deck.pop())
            people[2].hand.append(deck.pop())
            people[3].hand.append(deck.pop())

        # put a start card on a table

        put.append(deck.pop())

        # game start
        direction = 1
        i = 0
        j = 0
        while True:
            current_person = people[i % len(people)]
            selected = turn(current_person)
            if len(current_person.hand) == 0:
                # GUI(current_person.name 승리)
                break
            
            # Shape-changing card
            if selected == '7':
                # GUI(바꿀 모양(♥♣♠◆)의 index를 s에 입력받기)
                s = 1
                put[-1] = [shapes[s], 0]

            # K, Q, J        
            if direction:
                if selected == 'Q':
                    direction = 0  
                    i -= 1
                elif selected == 'J':
                    i += 2  
                elif selected != 'K':        
                    i += 1

            else:
                if selected == 'Q':
                    direction = 1
                    i += 1
                elif selected == 'J':
                    i -= 2
                elif selected != 'K':        
                    i -= 1

            if i < 0:
                i += len(people)