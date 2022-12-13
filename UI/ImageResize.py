import sys,os
sys.path.append(os.path.abspath(os.getcwd() + os.pardir))
print(os.path.abspath(os.path.join(os.getcwd() + os.pardir)))

from PIL import Image
from Game.Card import Card

shapes = '♥♣♠◆'
nums = []
deck  =[]

for i in range(2, 11):
    nums.append(str(i))
    for c in 'JQKA':
        nums.append(c)

for shape in shapes:
    for num in nums:
        deck.append((shape, num))

deck.append(('Joker', 'black'))
deck.append(('Joker', 'colored'))

for card in deck:
    data = Card.getCardImage(card)
    if not os.path.isfile('PNG-cards-1.3_resize' + data[13:-1:1] + 'g'):
        img = Image.open(data)
        img_resize_lanczos = img.resize((80, 120), Image.LANCZOS)
        result = 'PNG-cards-1.3_resize' + data[13:-1:1] + 'g'
        img_resize_lanczos.save(result)
    print("Success " + data)

data = "PNG-cards-1.3/background.png"

if not os.path.isfile("background_resize.png"):
    img = Image.open(data)
    img_resize_lanczos = img.resize((80, 120), Image.LANCZOS)
    result = 'PNG-cards-1.3_resize' + data[13:-1:1] + 'g'
    img_resize_lanczos.save(result)
print("Success " + data)
