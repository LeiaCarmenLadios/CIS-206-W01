import Card as Card_library
import Deck as Deck_library 
import Hand as Hand_library
import Player as Player_library
import Game as Game_library


if __name__ == "__main__":
       
    while True:
      game = Game_library.Game()
      while True:
         print("\n\n\tWelcome to the game of GO FISH!!!")
         print("Type \'Quit\' when asked to enter a card to exit.")
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
            if len(game.player_list) == 1:
               game_over = True
               game.finished_players.append(current_player)
               score_max = 0
               for i in range(len(game.finished_players)):
                  if game.finished_players[i].score > score_max:
                     score_max = game.finished_players[i].score
               for i in range(len(game.finished_players)):
                     if game.finished_players[i].score == score_max:
                        print(f"\nThe winner(s) is/are: Name: {game.finished_players[i].name}  Score: {game.finished_players[i].score}")   
               break
            card_correct = True   
            if len(current_player.player_hand.hand_cards) == 0:
               for _ in range(5):
                  if (len(game.game_deck.deck_of_cards) > 0):
                     crd = game.game_deck.draw()
                     print(f'{current_player.name} drew {crd}')
                     current_player.player_hand.addToHand(crd.card_value, crd.card_suit)
                  else:
                     card_correct = False
                     game.finished_players.append(current_player)
                     game.player_list.remove(current_player)
                     break
            while card_correct:
               if len(current_player.player_hand.hand_cards) <= 0:
                  break    
               print(f"There are {len(game.game_deck.deck_of_cards)} left to draw.")
               print(current_player) 
               print(f"\nIt is {current_player.name}'s turn...")
               print(f"{current_player.name}'s hand:")
               card_asked_for = current_player.askForCard()
               card_correct = game.askAnotherPlayer(current_player, card_asked_for)
               if card_correct == False and len(game.game_deck.deck_of_cards) > 0:
                  print("Card not in that player's hand. GO FISH!!!!")
                  crd = game.game_deck.draw()
                  print(f"\n{current_player.name} drew {crd}")
                  if crd != None:
                     current_player.player_hand.addToHand(crd.card_value, crd.card_suit)
               elif card_correct == False:
                  print("Card not in that player's hand. Change turns.")
               elif card_correct == True:
                  print("Correct! Card found.")
               game.checkFour(current_player)               
      break
               
   # game = Game_library.Game()
   # game.addPlayers('Leia')
   # game.addPlayers('Jacob')
   # #game.deal()
   # game.player_list[1].player_hand.addToHand('K','♢')
   # game.player_list[1].player_hand.addToHand('K','♡')
   # game.player_list[1].player_hand.addToHand('K','♤')
   # game.player_list[1].player_hand.addToHand('K','♧')
   # game.player_list[0].player_hand.addToHand('A','♢')
   # game.player_list[0].player_hand.addToHand('A','♡')
   # game.player_list[0].player_hand.addToHand('A','♤')
   # game.player_list[0].player_hand.addToHand('A','♧')
   
   # game.checkFour(game.player_list[1])
   # game.checkFour(game.player_list[0])
   

   # print(game.player_list[1]) 
   # print(game.player_list[0]) 
   # print(game.player_list[0].name, game.player_list[0].player_hand)
   # print(game.player_list[1].name, game.player_list[1].player_hand)
   # save_card = game.player_list[0].askForCard()
   # game.askAnotherPlayer(game.player_list[0],save_card)
   # print(game.player_list[0].name, game.player_list[0].player_hand)
   # print(game.player_list[1].name, game.player_list[1].player_hand)
   # bol_check = game.checkRequest(game.player_list[0], game.player_list[1], save_card)
   # print(bol_check)
