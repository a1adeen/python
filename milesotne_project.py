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
# player class
class Player:
    def __init__(self , name):
        self.name = name
        self.all_cards = []


    def remove_card(self):
        return self.all_cards.pop(0)

    def add_card(self , new_cards):
        # when there is more than 1 card to add
       if type(new_cards) == type([]):
           return self.all_cards.extend(new_cards)
       # when there is only 1 card to add
       else:
           self.all_cards.append(new_cards)

    def __str__(self):
        return f"{self.name} have {len(self.all_cards)} cards"



                                        # Game logic
                 # game setup          #while game on             #while at war




player_1 =  Player("one")
player_2 =  Player("two")


new_gameDeck = Deck()
new_gameDeck.shuffle()

# to give cards to both of them


for x in range(26):
    player_1.add_card(new_gameDeck.get_one())
    player_2.add_card(new_gameDeck.get_one())

# print(len(player_1.all_cards))

# starting game

game_on = True
rounds = 0

while game_on:
    rounds += 1
    print(f"round {rounds}")



    if len(player_1.all_cards) == 0:
        print(f"player_1 , out of cards PLAYER 2 wins the game!!!!")
        game_on = False
        break


    if len(player_2.all_cards) == 0 :
        print(f"player_1 , out of cards PLAYER 2 wins the game!!!!")
        game_on = False
        break



# start a new round

player_1_cards = []
player_1_cards.append(player_1.remove_card())

player_2_cards = []
player_2_cards.append(player_2.remove_card())



# while at war



at_war = True

while at_war:
    if player_1_cards[-1].value > player_2_cards[-1].value:
        player_1_cards.append(player_1_cards)
        player_1_cards.append(player_2_cards)

        at_war = False
    elif  player_1_cards[-1].value < player_2_cards[-1].value:
        player_2_cards.append(player_1_cards)
        player_2_cards.append(player_2_cards)

        at_war = False

    else:
        print("WAR!!!!")


        if len(player_1_cards) < 3:
            print("player_1 is unable to declare the war ")
            print("player 2 wins ")

            game_on = False
            break


        elif len(player_2_cards) < 3:
            print("player_2 is unable to declare the war ")
            print("player 1 wins ")

            game_on= False
            break

        else:
            for num in range(3):
                player_1_cards.append(player_1.remove_card())
                player_2_cards.append(player_2.remove_card())
he = 8


        # new_deck = Deck()
# new_deck.shuffle()
# mycard = new_deck.get_one()
# print(mycard)
# hiten = Player("hiten")
# hiten.add_card(mycard)
# hiten.add_card([mycard , mycard])
# print(hiten)
# #
# # choosing cards form here
# deck_card = Deck()
# # when we use this all the cards got shuffles in a deck
# deck_card.shuffle()
# # here is the card to show that the deck is shuffling
# print(deck_card.all_cards[-1])
# # poping card from the deck
# print(deck_card.get_one())
