import Card as Card_library
import Deck as Deck_library
import Hand as Hand_library
import Game as Game_library
import Player as Player_library
import unittest
import sys
import io


class TestPlayer(unittest.TestCase):

    def test_player_isinstance_of_player_class(self):
        player = Player_library.Player()
        message = "Object is not instance of Player class"
        self.assertIsInstance(player, Player_library.Player, message)   

    def test_player_default_initializes_default_name_correct(self):
        player = Player_library.Player()
        self.assertEqual(player.name, "Player")

    def test_player_default_initializes_score_correct(self):
        player = Player_library.Player()
        message = "Player score not initialized to zero correctly."
        self.assertEqual(player.score, 0, message)

    def test_player_default_initializes_books_to_empty_list_correct(self):
        player = Player_library.Player()
        message = "Player attribute books not intialized to empty list properly."
        self.assertEqual(player.books, [], message)
    
    def test_player_initializes_name_from_initializer(self):
        player = Player_library.Player("Joe")
        message = "__init__ not initializing name properly."
        self.assertEqual(player.name, "Joe", message)

    def test_player_default_initializes_instance_player_hand_object_correct(self):
        player = Player_library.Player()
        message = "Player Hand Object is not instance of Hand class"
        self.assertIsInstance(player.player_hand, Hand_library.Hand, message)

    def test_player_default_initializes_player_hand_object_to_empty(self):
        player = Player_library.Player()
        message = "Initialized Player's Hand object's hand_cards should be empty list"
        self.assertEqual(player.player_hand.hand_cards, [], message)

    def test_player_string_magic_method_outputs(self):
        player = Player_library.Player("Joe")
        value_check = player.__str__()
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(player, end='')
        sys.stdout = sys.__stdout__
        message = "__str__ method output displaying incorrect."
        self.assertEqual(capturedOutput.getvalue(), value_check, message)
        self.assertEqual(value_check, '\nName: Joe Score: 0 Books: []', message)

    def test_player_askForCard_returns_correct_card_object_uppercase(self): 
        player = Player_library.Player()
        input_values = ['A']
        def input(prompt=None):
            return input_values.pop()
        Player_library.input = input
        asked_card = player.askForCard()
        self.assertEqual(asked_card.card_value, 'A')
        self.assertEqual(asked_card.card_suit, '♡')

    def test_player_askForCard_returns_correct_card_object_lowercase(self): 
        player = Player_library.Player()
        input_values = ['a']
        def input(prompt=None):
            return input_values.pop()
        Player_library.input = input
        asked_card = player.askForCard()
        self.assertEqual(asked_card.card_value, 'A')
        self.assertEqual(asked_card.card_suit, '♡')

    @unittest.skip("Not working")
    def test_player_askForCard_validation_incorrect_card_entered(self): 
        player = Player_library.Player()
        input_values = ['A of elbow']
        def input(prompt=None):
            return input_values.pop()
        player.askForCard()
        player.input = input
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), 'Invalid card. Try Again\nEx: A of ♧ or A of spade\n')

    def test_player_addToScore_adds_correct(self):
        player = Player_library.Player()
        self.assertEqual(player.score, 0, "Player score not initialized to 0")
        player.addToScore()
        self.assertEqual(player.score, 1, "Player score not adding correctly")


if __name__ == '__main__':
    unittest.main()