class Card:

    def __init__(self, value, suit):
        if value == 11:
            self.value = "Jack"
        elif value == 12:
            self.value = "Queen"
        elif value == 13:
            self.value = "King"
        elif value == 1:
            self.value = "Ace"
        else:
            self.value = str(value)
        self.value = value
        self.suit = suit

    def __str__(self):
        return f" {self.value} of {self.suit}."
