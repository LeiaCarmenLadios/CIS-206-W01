import unittest
import Deck as Deck_library
import Card as Card_library
import io
import sys
import copy

class TestDeck(unittest.TestCase):

    def test_deck_initializes_correct(self):
        deck = Deck_library.Deck()
        first_crd = Card_library.Card('A','♧') # test that first card vliue and last card value on the created deck is correct 
        last_crd = Card_library.Card('K', '♤') # and deck is populated correctly
        value_check = [first_crd._card_value, first_crd._card_suit, last_crd._card_value, last_crd._card_suit]
        deck_values = [deck._deck_of_cards[0]._card_value, deck._deck_of_cards[0]._card_suit, deck._deck_of_cards[51]._card_value, deck._deck_of_cards[51]._card_suit]
        self.assertEqual(deck_values, value_check)

    def test_deck_length_correct(self):
        deck = Deck_library.Deck()
        self.assertEqual(len(deck.deck_of_cards), 52)
        
    def test_deck_resets_correct(self):
        deck = Deck_library.Deck()
        deck.reset()
        first_crd = Card_library.Card('A','♧') # test that first card vliue and last card value on the created deck is correct 
        last_crd = Card_library.Card('K', '♤') # and deck is populated correctly
        value_check = [first_crd._card_value, first_crd._card_suit, last_crd._card_value, last_crd._card_suit]
        deck_values = [deck._deck_of_cards[0]._card_value, deck._deck_of_cards[0]._card_suit, deck._deck_of_cards[51]._card_value, deck._deck_of_cards[51]._card_suit]
        self.assertEqual(deck_values, value_check)

    def test_deck_correct_valuesuits(self):
        VALUE = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        SUIT = ['♧', '♢', '♡', '♤']
        deck = Deck_library.Deck()
        for card in deck._deck_of_cards:
            self.assertIn(card.card_value, VALUE)
        for card in deck._deck_of_cards:
            self.assertIn(card.card_suit, SUIT)

    def test_deck_string_magic_method_outputs(self):
        deck = Deck_library.Deck()
        value_check = deck.__str__()
        self.assertEqual(value_check[0:7], 'A of ♧\n')

    def test_deck_draw_correct(self):
        deck = Deck_library.Deck()
        last_crd = Card_library.Card('K', '♤')
        value_check = [last_crd._card_value, last_crd._card_suit]
        crd = deck.draw()
        draw_check = [crd._card_value, crd._card_suit]
        self.assertEqual(draw_check, value_check)

    def test_deck_shuffle_correct(self):
        deck1 = Deck_library.Deck()
        deck2 = copy.deepcopy(deck1)
        deck2.shuffle()
        self.assertNotEqual(deck1.deck_of_cards, deck2.deck_of_cards)
        self.assertEqual(len(deck1.deck_of_cards), len(deck2.deck_of_cards))
        for card in deck1._deck_of_cards:
            self.assertIn(card.__str__(), deck2.__str__())
        for card in deck2._deck_of_cards:
            self.assertIn(card.__str__(), deck1.__str__())
            
if __name__ == '__main__':
    unittest.main()
    
