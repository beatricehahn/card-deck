# Card class

# CardRequirements:

# Each instance should have a suit: "Hearts", "Diamonds", "Clubs", or "Spades"
# Each instance will have a value: ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
# Card 's __repr__  method should return the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)

class Card:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    @classmethod
    def valid_card(cls):
        pass

    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
    
    def __repr__(self):
        return f" {self.value} of {self.suit}"