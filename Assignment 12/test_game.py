import Card as Card_library
import Deck as Deck_library
import Hand as Hand_library
import Game as Game_library
import Player as Player_library
import unittest

class TestPlayer(unittest.TestCase):
    
    def test_game_isinstance_of_game_class(self):
        game = Game_library.Game()
        message = "Object is not instance of Game class"
        self.assertIsInstance(game, Game_library.Game, message)   

    def test_game_default_initializes_instance_game_deck_object_correct(self):
        game = Game_library.Game()
        message = "Game - Deck Object is not instance of Deck class"
        self.assertIsInstance(game.game_deck, Deck_library.Deck, message)

    def test_game_default_initializes_player_list_to_empty_list_correct(self):
        game = Game_library.Game()
        message = "Game - Player list attribute not intialized to empty list properly."
        self.assertEqual(game.player_list, [], message)


if __name__ == '__main__':
    unittest.main()
