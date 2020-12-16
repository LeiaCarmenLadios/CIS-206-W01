import Card as Card_library
import Deck as Deck_library
import Hand as Hand_library
import Game as Game_library
import unittest
import sys
import io

class TestHand(unittest.TestCase):

    def test_hand_isinstance_of_hand_class(self):
        hand = Hand_library.Hand()
        self.assertIsInstance(hand, Hand_library.Hand, "Object is not instance of Hand class")  

    def test_hand_initializes_correct(self):
        hand = Hand_library.Hand()
        self.assertEqual(len(hand.hand_cards), 0)

    def test_hand_intitializes_correct2(self):
        hand = Hand_library.Hand()
        self.assertEqual(type(hand.hand_cards), list)

    def test_hand_addToHand(self, value='A', suit='♡'):
        hand = Hand_library.Hand()
        hand.addToHand(value,suit)
        added_card = [hand.hand_cards[0].card_value, hand.hand_cards[0].card_suit]
        hand_test = ['A','♡']
        self.assertEqual(added_card, hand_test)  
    
    def test_hand_removeFromHand(self, value='A'):
        hand = Hand_library.Hand()
        hand.addToHand('A','♡')
        hand.addToHand('K','♤')
        hand.removeFromHand(value)
        remaining_card = [hand.hand_cards[0].card_value, hand.hand_cards[0].card_suit]
        hand_test = ['K','♤']
        self.assertEqual(remaining_card, hand_test)

    def test_hand_string_magic_method_outputs(self):
        hand = Hand_library.Hand()
        hand.addToHand('A','♧')
        value_check = hand.__str__()
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(hand, end='')
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), value_check)
        self.assertEqual(value_check[0:7], 'A of ♧\n')

    # @unittest.skip
    # def test_hand_maxHand(self):
    #     hand = Hand_library.Hand()
    #     game = Game_library.Game()
    #     max_hand_length = 0
    #     if(len(game._player_list) == 2) || (len(game._player_list) == 3)
    #         max_hand_length = 7
    #     elif(len(game._player_list) == 4) && (len(game._player_list) == 5)
    #         max_hand_length = 5
    #     else:
    #         max_hand_length = 0

if __name__ == '__main__':
    unittest.main()
     
