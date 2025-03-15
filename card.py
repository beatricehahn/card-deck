# Card class

# CardRequirements:

# Each instance should have a suit: "Hearts", "Diamonds", "Clubs", or "Spades"
# Each instance will have a value: ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
# Card 's __repr__  method should return the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)

class Card:
    def __init__(self, val, suit):
        self.value = val
        self.suit = suit
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"