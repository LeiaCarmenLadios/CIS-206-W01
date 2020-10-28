import unittest
import Card as Card_library
import io
import sys

class TestCard(unittest.TestCase):

    def test_card_initializes_correct(self):
        crd = Card_library.Card('A', 'P')
        crd_values = [crd._card_value, crd._card_suit]
        value_check = ['A', 'P']
        self.assertEqual(crd_values, value_check)

    def test_card_string_magic_method_outputs(self):
        crd = Card_library.Card('A', 'D')
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(crd)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), 'A of D\n')

    def test_card_property(self): # Not sure a property really needs to be tested
        crd = Card_library.Card('A', 'P')
        crd_suit = crd._card_suit
        crd_value = crd._card_value
        self.assertEqual(f'{crd.card_value} of {crd.card_suit}', f'{crd_value} of {crd_suit}')

if __name__ == '__main__':
    unittest.main()
