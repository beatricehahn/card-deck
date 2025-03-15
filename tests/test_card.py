from unittest import TestCase
from card import Card

class TestCardClass(TestCase):
    def test_card_initialization(self):
        # Create an Ace of Spades and check value and suit
        card = Card("Ace", "Spades")
        self.assertEqual(card.value, "Ace")
        self.assertEqual(card.suit, "Spades")
