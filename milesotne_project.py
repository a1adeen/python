# card game
import random



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

                createrd_crads = (suit , rank)

                self.all_cards.append(createrd_crads)

# new_deck = Deck()
# print(new_deck.all_cards[-1])