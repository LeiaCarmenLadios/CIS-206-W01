import Hand as Hand_library
import Card
import Deck

class Player:
    name = "Player"
    player_hand = Hand_library.Hand()
    is_playing = False
    score = 0
    books = []
    
    def __init__(self, name):
        self.name = name

    # def checkFour(self):
    #     counter = 0 
        
        # for i in len(hand):# 
        #     :
        #         pass
    def askPlayer(self):
        askplayer_player = input("Which player would you like to ask? [name of player]") # string
        askplayer_card = input("which card would you like to ask for? [card value]") # string
        if askplayer_card in self.player_hand:
            if askplayer_card in askplayer_player.player_hand:
                pass # PLACEHOLDER
        else:
            pass # PLACEHOLDER

        