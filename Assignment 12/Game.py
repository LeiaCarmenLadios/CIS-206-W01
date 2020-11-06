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
         self._player_list = []
      
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
         to_remove = []
         counter = 1
         for i in range(len(player_hand_list)):
            check_card = player_hand_list[i]
            if (i+1) < (len(player_hand_list)):
               if player_hand_list[i+1] == check_card: 
                  counter += 1
               if counter == 4:
                  to_remove.append(check_card)
                  counter = 1
         for ix in to_remove:
            player.player_hand.removeFromHand(to_remove[ix])
         print(player.player_hand)

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
            if plyr.name == name_of_player:
               player_asked_for = plyr
         if name_of_player == player_asked_for.name:
            is_found = self.checkRequest(current_player_obj, player_asked_for, card_needed)
         else:
            print("There is no player with that name. Please try again.")  
         return is_found        


if __name__ == "__main__":
   # game = Game()
   # game.addPlayers('Leia')
   # game.addPlayers('Jacob')
   # game.deal()
   # game.player_list[1].player_hand.addToHand('K','♢')
   # game.player_list[1].player_hand.addToHand('K','♡')
   # print(game.player_list[0].name, game.player_list[0].player_hand)
   # print(game.player_list[1].name, game.player_list[1].player_hand)
   # save_card = game.player_list[0].askForCard()
   # game.askAnotherPlayer(game.player_list[0],save_card)
   # print(game.player_list[0].name, game.player_list[0].player_hand)
   # print(game.player_list[1].name, game.player_list[1].player_hand)
   # bol_check = game.checkRequest(game.player_list[0], game.player_list[1], save_card)
   # print(bol_check)
    
    while True:
      game = Game()
      while True:
         print("\n\n\tWelcome to the game of GO FISH!!!")
         print("\nHow many players will be playing? (minimum 2; maximum 5): ")
         num_of_players = int(input())
         print()
         if num_of_players < 2:
            print("You need more than 1 player.")
         elif num_of_players > 5:
            print("You have entered more than the maximum(5) number of players.")
         else:
            break 
      
      for _ in range(num_of_players):   
         print("Please enter the name of a player:")
         name = input()
         game.addPlayers(name)  
      
      game.deal()
      
      game_over = False
      while not game_over:
         for current_player in game.player_list:
            game.checkFour(current_player)
            card_correct = True
            while card_correct:
               print(f"\nIt is {current_player.name}'s turn...")
               print(f"{current_player.name} hand:")
               card_asked_for = current_player.askForCard()
               card_correct = game.askAnotherPlayer(current_player, card_asked_for)
               if card_correct == False:
                  print("Card not in that player's hand.")
               else:
                  print("Correct! Card found. You get another turn!!")
               game.checkFour(current_player)
            

