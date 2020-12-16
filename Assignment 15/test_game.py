import Card as Card_library
import Deck as Deck_library
import Hand as Hand_library
import Game as Game_library
import Player as Player_library
import unittest
from unittest import mock
import io
import sys

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
        message = "Game - player_list attribute not intialized to empty list properly."
        self.assertEqual(game.player_list, [], message)

    def test_game_default_initializes_finished_player_list_to_empty_list_correct(self):
        game = Game_library.Game()
        message = "Game - finished_players list attribute not intialized to empty list properly."
        self.assertEqual(game.finished_players, [], message)

    def test_game_addPlayers_adds_players_to_playerlist(self):
        game = Game_library.Game()
        message = "Game - player_list did not initialize to empty list"
        self.assertEqual(len(game.player_list), 0, message)
        game.addPlayers("Joe")
        message2 = "Game - addPlayers() did not add player to player_list"
        self.assertEqual(len(game.player_list), 1, message2)
        self.assertEqual(game.player_list[0].name, "Joe", message2)

    def test_game_print_player_list_prints_correctly(self):
        game = Game_library.Game()
        game.addPlayers("Joe")
        game.addPlayers("Schmoe")
        value_check = game.print_player_list()
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(game.print_player_list(), end='')
        sys.stdout = sys.__stdout__
        message = "Game - print_player_list did not print correctly"
        self.assertEqual(capturedOutput.getvalue(), "Players: (Joe, Schmoe)")
        self.assertEqual(value_check, capturedOutput.getvalue(), message)

    def test_game_deal_distributes_five_cards(self):
        game = Game_library.Game()
        game.addPlayers("Joe")
        game.addPlayers("Schmoe")
        game.deal()
        message = "Player was dealt incorrect amount of cards"
        self.assertEqual(len(game.player_list[0].player_hand.hand_cards), 5, message)
        self.assertEqual(len(game.player_list[1].player_hand.hand_cards), 5, message)
        message2 = "Remaining deck has the wrong amount of cards"
        self.assertEqual(len(game.game_deck.deck_of_cards), 52 - 5 * (len(game.player_list)), message2)

    def test_game_checkFour_method(self):
        game = Game_library.Game()
        game.addPlayers("Joe")
        crd = Card_library.Card('A', '♢')
        game.player_list[0].player_hand.addToHand(crd.card_value, crd.card_suit)
        crd2 = Card_library.Card('A', '♤')
        game.player_list[0].player_hand.addToHand(crd2.card_value, crd2.card_suit)
        crd3 = Card_library.Card('2', '♡')
        game.player_list[0].player_hand.addToHand(crd3.card_value, crd3.card_suit)
        crd4 = Card_library.Card('A', '♧')
        game.player_list[0].player_hand.addToHand(crd4.card_value, crd4.card_suit)
        crd5 = Card_library.Card('A', '♡')
        game.player_list[0].player_hand.addToHand(crd5.card_value, crd5.card_suit)
        game.checkFour(game.player_list[0])
        message = "checkFour did not add to books properly."
        self.assertEqual(len(game.player_list[0].books), 1, message)
        message2 = "checkFour did not add the proper card_value to books properly."
        self.assertEqual(game.player_list[0].books, ['A'], message2)
        message3= "checkFour did not add to score properly."
        self.assertEqual(game.player_list[0].score, 1, message3)

    def test_game_checkFour_method_removeBooksFromHand(self):
        game = Game_library.Game()
        game.addPlayers("Joe")
        crd = Card_library.Card('A', '♢')
        game.player_list[0].player_hand.addToHand(crd.card_value, crd.card_suit)
        crd2 = Card_library.Card('A', '♤')
        game.player_list[0].player_hand.addToHand(crd2.card_value, crd2.card_suit)
        crd3 = Card_library.Card('2', '♡')
        game.player_list[0].player_hand.addToHand(crd3.card_value, crd3.card_suit)
        crd4 = Card_library.Card('A', '♧')
        game.player_list[0].player_hand.addToHand(crd4.card_value, crd4.card_suit)
        crd5 = Card_library.Card('A', '♡')
        game.player_list[0].player_hand.addToHand(crd5.card_value, crd5.card_suit)
        game.checkFour(game.player_list[0])
        message = "checkFour removed the cards with four matches from player hand."
        self.assertEqual(len(game.player_list[0].player_hand.hand_cards), 1, message)

    @unittest.skip("Need to enter input manually")
    def test_game_AskAnotherPlayer(self): 
        game = Game_library.Game()
        game.addPlayers("Joe")
        game.addPlayers("John")
        crd = Card_library.Card('A', '♢')
        game.player_list[1].player_hand.addToHand(crd.card_value, crd.card_suit)
        crd2 = Card_library.Card('2', '♡')
        game.player_list[1].player_hand.addToHand(crd2.card_value, crd2.card_suit)
        def player_input():
            game.askAnotherPlayer(game.player_list[0], crd)
            mock.builtins.input = lambda _: "John"
        player_input()
        self.assertEqual(game.player_list[0].player_hand.hand_cards[0].card_value, 'A')
        self.assertEqual(game.player_list[0].player_hand.hand_cards[0].card_suit, '♢')

        # def bar():
        # ans = input("enter yes or no")
        # if ans == "yes":
        # return "you entered yes"
        # if ans == "no":
        # return "you entered no"
        
        # def test_bar_yes():
        # original_input = mock.builtins.input
        # mock.builtins.input = lambda _: "yes"
        # assert_equal(bar(), "you entered yes")
        # mock.builtins.input = original_input

if __name__ == '__main__':
    unittest.main()