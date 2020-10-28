import Card as Card_library
import Deck as Deck_library 
import Hand as Hand_library
import Player as Player_library

class Game:
     @property
     def game_deck(self):
        return self._game_deck

     def __init__(self):
        self._game_deck = Deck_library.Deck()
        player1 = Player_library.Player('player1')
        player2 = Player_library.Player('player2')
        self.player_list = [player1, player2]

     def deal(self):
        self._game_deck.shuffle()
        print("asdhkjdfhalfhurtbjfka.jdfhliguhr")
        # for player in self.player_list:
        #     player.player_hand.append(Deck.)

if __name__ == "__main__":
    game = Game()
    print(game.game_deck)
    game.deal()
    print(game.game_deck)
       
