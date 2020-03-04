from deck_of_cards import Card
from deck_of_cards import Deck
import unittest

class CardTest(unittest.TestCase):
    def setUp(self):
        self.card = Card("A", "Spades")

    def test_init(self):
        """cards should have a suit and a value"""
        self.assertEqual(self.card.suit, "Spades")
        self.assertEqual(self.card.value, "A")
        
    def test_repr(self):
        """Cards should display as VALUE of SUIT"""
        self.assertEqual(repr(self.card), "A of Spades")

class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        """decks should have a cards attribute that is an instance of a list and a count of 52"""
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertEqual(len(self.deck.cards), 52)

    def test_repr(self):
        """Deck should display 'Deck of 52' cards"""
        self.assertEqual(repr(self.deck), "Deck of 52 cards.")

    def test_count(self):
        """Should return a length of 52"""
        self.assertEqual(self.deck.count(), 52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 51)

    def test_deal_sufficient_cards(self):
        """Test that deal deals the proper number of cards and the number of leftover cards is accurate"""
        cards = self.deck._deal(10)
        self.assertEqual(len(cards), 10)
        self.assertEqual(self.deck.count(), 42)

    def test_deal_insufficient_cards(self):
        """Test that deal cannot deal more cards than available and the number of leftover cards is 0"""
        cards = self.deck._deal(100)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.deck.count(), 0)

    def test_insufficient_shuffle(self):
        """Anything less than a full deck should return a ValueError"""
        self.deck._deal(1)
        with self.assertRaises(ValueError):
            self.deck.shuffle()

    def test_sufficient_shuffle(self):
        """Should shuffle the deck and """
        cards = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(cards, self.deck.cards)
        self.assertEqual(self.deck.count(), 52)

if __name__ == '__main__':
    unittest.main()
    