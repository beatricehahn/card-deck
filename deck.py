from card import Card
from random import shuffle

# Deck requirements:

# Each instance of Deck  should have a cards attribute with all 52 possible instances of Card
# Deck  should have an instance method called count  which returns a count of how many cards remain in the deck
# Deck 's __repr__  method should return information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
# Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards from the end of the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should return a ValueError  with the message "All cards have been dealt"
# Deck  should have an instance method called shuffle  which will shuffle a full deck of cards. If there are cards missing from the deck, this method should raise a ValueError  with the message "Only full decks can be shuffled". shuffle should return the shuffled deck.
# Deck  should have an instance method called deal_card  which uses the _deal  method to deal a single card from the deck and return that single card
# Deck  should have an instance method called deal_hand  which accepts a number and uses the _deal  method to deal a list of cards from the deck and return that list of cards

class Deck:
    def __init__(self):
        SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
        VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(value, suit) for suit in SUITS for value in VALUES]

    def count(self):
        return len(self.cards)
    
    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def _deal(self, num):
        # check how many cards are in the deck
        count = self.count()
        # determine the smaller value to use for taking out cards
        actual = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        # save the cards to be dealt in cards_to_deal, taking from the end of the deck
        cards_to_deal = self.cards[-actual:]
        # update deck
        self.cards = self.cards[:-actual]
        return cards_to_deal

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)