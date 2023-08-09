# card game
import random
from random import shuffle



suits = ( 'Clubs','Diamonds','Hearts','Spades')
ranks = ("ace" , "two" , "three" , "four" , "five" , "six" , "seven" ,"eight" , "nine" , "ten" , "jack" , "king" , "queen")
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
card_3 = card("spades" , 13)
card_4 = card("clubs" , 9)



if (card_1.value < card_2.value):
    print("card_2 is greater than the card_1 ")
else:
    print("card_1 is greater than the card_2")


# other comparision
if card_3.value == card_4.value:
    print("true")
else:
    print("false")
# print(card_1.value)

# deck class
class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:

                createrd_crads = f"{rank} of {suit}"

                self.all_cards.append(createrd_crads)
# to shuffle the deck
    def shuffle(self):
            random.shuffle(self.all_cards)


# to take thesingle card from the deck

    def get_one(self):
       return self.all_cards.pop()





# choosing cards form here
deck_card = Deck()
# when we use this all the cards got shuffles in a deck
deck_card.shuffle()
# here is the card to show that the deck is shuffling
print(deck_card.all_cards[-1])
# poping card from the deck
print(deck_card.get_one())
