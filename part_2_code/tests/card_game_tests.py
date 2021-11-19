import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card_ace = Card("diamonds", 1)
        self.card_9 = Card("spades", 9)
        self.card_jack = Card("spades", 11)
        self.cardgame = CardGame()
        
    def test_check_for_ace__card_is_ace(self):
        result = self.cardgame.check_for_ace(self.card_ace)
        self.assertEqual(result, True)

    def test_check_for_ace__card_is_not_ace(self):
        result = self.cardgame.check_for_ace(self.card_9)
        self.assertEqual(result, False)

    def test_highest_card__card1_is_highest(self):
        result = self.cardgame.highest_card(self.card_9, self.card_ace)
        self.assertEqual(result.value, 9)

    def test_highest_card__card2_is_highest(self):
        result = self.cardgame.highest_card(self.card_9, self.card_jack)
        self.assertEqual(result.value, 11)

    def test_cards_total__21(self):
        cards = []
        cards.append(self.card_ace)
        cards.append(self.card_9)
        cards.append(self.card_jack)
        result = self.cardgame.cards_total(cards)
        self.assertEqual(result, "You have a total of 21")
        