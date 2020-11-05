import Card as Card_library
import Deck as Deck_library 
import Hand as Hand_library
import Player as Player_library

class Game:
      @property
      def game_deck(self):
         return self._game_deck

      @property 
      def player_list(self):
         return self._player_list


      def __init__(self):
         self._game_deck = Deck_library.Deck()
         player1 = Player_library.Player('player1')
         player2 = Player_library.Player('player2')
         self._player_list = [player1, player2]

      def deal(self):
         self._game_deck.shuffle()
         # for player in self.player_list:
         #     player.player_hand.append(Deck.)

      def checkFour(self, player):
         # crd = Card_library.Card('A', '♢')
         # player.player_hand.addToHand(crd.card_value, crd.card_suit)
         # crd2 = Card_library.Card('A', '♤')
         # player.player_hand.addToHand(crd2.card_value, crd2.card_suit)
         # crd3 = Card_library.Card('2', '♡')
         # player.player_hand.addToHand(crd3.card_value, crd3.card_suit)
         # crd4 = Card_library.Card('A', '♧')
         # player.player_hand.addToHand(crd4.card_value, crd4.card_suit)
         # crd5 = Card_library.Card('A', '♡')
         # player.player_hand.addToHand(crd5.card_value, crd5.card_suit)

         player_hand_list = []
         for ix in range(len(player.player_hand.hand_cards)):
            player_hand_list.append(player.player_hand.hand_cards[ix].card_value)
         player_hand_list.sort()
         to_remove = []
         # for phl_value in range(len(player_hand_list)):
         
         counter = 1
         for i in range(len(player_hand_list)):
            check_card = player_hand_list[i]
            if (i+1) < (len(player_hand_list)):
               if player_hand_list[i+1] == check_card: 
                  counter += 1
               if counter == 4:
                  to_remove.append(check_card)
                  counter = 1

         print('to_remove = ', to_remove)
         print(player.player_hand)
         for ix in to_remove:
            player.player_hand.removeFromHand(crd.card_value)
         print(player.player_hand)

                   
            


if __name__ == "__main__":
    game = Game()
    game.deal()
   #  print(game.game_deck)
    game.checkFour(game.player_list[0])
        # issues: the deck does not seem to be shuffling. I tested the shuffle method in the Deck class and it works just fine there. 
        # I think there's something wrong in that the shuffled deck is not actually being saved in the game deck. 
