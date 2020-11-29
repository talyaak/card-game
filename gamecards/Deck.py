from gamecards.Card import Card
from random import shuffle, randrange


class DeckOfCards:

    def __init__(self):  # operator
        self.deck = []
        self.dealt = []  # Prevents from dealing the same card
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:  # creates an organized deck
            for rank in range(1, 14):  # grants the card a title
                if rank == 11:
                    value = "Jack"
                elif rank == 12:
                    value = "Queen"
                elif rank == 13:
                    value = "King"
                elif rank == 1:
                    value = "Ace"
                else:
                    value = str(rank)
                self.deck.append(Card(value, suit))

    def __repr__(self):  # __repr__ creates an organized string to print the deck
        str1 = ""
        for i in self.deck:
            str1 += i.__str__()
        return str1

    def deck_shuffle(self):  # shuffles the deck
        shuffle(self.deck)

    def deal_one(self):  # deals the user a card from the deck, and makes sure the same card will be dealt again
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]  # suit list
        while True:
            randValue = randrange(1, 14)  # generates a random value
            randSuit = randrange(1, 5)  # generates a random Suit number
            if Card(randValue, suits[randSuit]) not in self.dealt:  # using self.dealt so we don't hand out a card twice
                self.dealt.append(Card(randValue, suits[randSuit]))
                return Card(randValue, suits[randSuit])
            else:
                pass

    def show(self):

