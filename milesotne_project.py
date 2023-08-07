# card game
import random



suit = {
    0: 'Clubs',
    1: 'Diamonds',
    2: 'Hearts',
    3: 'Spades'
}
values = {
    1: 'Ace',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: '10',
    11: 'Jack',
    12: 'Queen',
    13: 'King'
}


class card:
    def __init__(self , suit , rank ):
        self.suit = suit
        self.rank = int(rank)
        self.value = values[rank]
    def __str__(self):
        return f"{self.rank} of {self.suit}"


# comparing here
card_1 = card("clubs" , 3)
card_2 = card("hearts" , 7)

if (card_1.value < card_2.value):
    print("card_2 is greater than the card_1 ")
else:
    print("card_1 is greater than the card_2")
# print(card_1.value)




