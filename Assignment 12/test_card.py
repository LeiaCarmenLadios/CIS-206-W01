import unittest
import Card as Card_library
import io
import sys

class TestCard(unittest.TestCase):

    def test_card_isinstance_of_card_class(self):
        crd = Card_library.Card('A', '♧')
        message = "Object is not instance of Card class"
        self.assertIsInstance(crd, Card_library.Card, message)   

    def test_card_initializes_correct(self):
        crd = Card_library.Card('A', '♧')
        crd_values = [crd._card_value, crd._card_suit]
        value_check = ['A', '♧']
        self.assertEqual(crd_values, value_check)

    def test_card_raises_on_invalid_valuesuit(self):
        with self.assertRaises(Exception):
            Card_library.Card('A', 'F')

    def test_card_string_magic_method_outputs(self):
        crd = Card_library.Card('A', '♤')
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(crd)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), 'A of ♤\n')

    def test_card_property(self): # Not sure a property really needs to be tested
        crd = Card_library.Card('A', '♤')
        crd_suit = crd._card_suit
        crd_value = crd._card_value
        self.assertEqual(f'{crd.card_value} of {crd.card_suit}', f'{crd_value} of {crd_suit}')

if __name__ == '__main__':
    unittest.main()
