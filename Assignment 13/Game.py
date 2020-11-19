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

      @property 
      def finished_players(self):
         return self._finished_players

      @property 
      def num_of_players(self):
         return self._num_of_players

      @num_of_players.setter
      def num_of_players(self, num):
         self._num_of_players = num

      def __init__(self):
         self._game_deck = Deck_library.Deck()
         self._player_list = []
         self._finished_players = []
         self.num_of_players = 0
      
      def addPlayers(self, playerName):
         player_to_add = Player_library.Player(playerName)
         self.player_list.append(player_to_add)

      def print_player_list(self):
         name_list = 'Players: ('
         for player in self.player_list:
            name_list += player.name + ", "
         name_list = name_list[:-2]
         return name_list + ')'
            

      def deal(self):
         self._game_deck.shuffle()
         counter = 5
         while(counter != 0):
            for player in self.player_list:
               card_deal = self.game_deck.deck_of_cards[len(self.game_deck.deck_of_cards)-1]
               self.game_deck.draw()
               player.player_hand.addToHand(card_deal.card_value, card_deal.card_suit)
            counter -= 1

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
         # print(player_hand_list)
         to_remove = []
         counter = 1
         something = len(player_hand_list)
         for i in range(something):
            check_card = player_hand_list[i]
            if (i+1) < (len(player_hand_list)):
               if player_hand_list[i+1] == check_card: 
                  counter += 1
               else:
                  counter = 1
               if counter == 4:
                  to_remove.append(check_card)
                  counter = 0

         for ix in to_remove:
            player.addToScore()
            player.books.append(ix)
            player.player_hand.removeFromHand(ix)

      def checkRequest(self, current_player, player_asked, card):
         is_found = False
         suits_to_transfer = []
         for crd in player_asked.player_hand.hand_cards:
            if crd.card_value == card.card_value:
               suits_to_transfer.append(crd.card_suit)
               is_found = True
         for suit in suits_to_transfer:
            player_asked.player_hand.removeFromHand(card.card_value)
            current_player.player_hand.addToHand(card.card_value, suit)
         return is_found


      def askAnotherPlayer(self, current_player_obj, card_needed):
         is_found = False
         print("\nWho would you like to ask a card from?")
         print(self.print_player_list())
         name_of_player = input()
         player_asked_for = Player_library.Player()
         print(player_asked_for.player_hand)
         for plyr in self.player_list:
            if plyr.name.lower() == name_of_player.lower():
               player_asked_for = plyr
         if name_of_player.lower() == player_asked_for.name.lower():
            is_found = self.checkRequest(current_player_obj, player_asked_for, card_needed)
         else:
            print("There is no player with that name. Please try again.")  
         return is_found        


if __name__ == "__main__":
   pass 
    
    
            
