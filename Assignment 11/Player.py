import Hand as Hand_library
import Card as Card_library
import Deck as Deck_library

class Player:
   
    @property # allows us to access the method like it's a property
    def name(self):
        return self._name

    @name.setter 
    def name(self, name):
        self._name = name

    @property 
    def is_playing(self):
        return self._is_playing

    @is_playing.setter
    def is_playing(self, is_playing):
        self._is_playing = is_playing

    @property 
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        self._score = score

    @property 
    def player_hand(self):
        return self._player_hand

    @property 
    def books(self):
        return self._books

    def __init__(self, name = "Player"):
        self.name = name
        self.is_playing = False
        self.score = 0
        self._books = []
        self._player_hand = Hand_library.Hand()

    def askForCard(self):
       
        # print out their hand so that they know what options are available to them
        # They can only ask for a card if they have at least one of that value card
        while True:
            print(self.player_hand)
            askplayer_card = input("Which card would you like to ask for? [card value]: ") # string 
            value_card,suit_card = askplayer_card.split(' of ')
            try:
                # ask_card = Card_library.Card() # defualt
                if suit_card[0].lower() == 'h' or suit_card == '♡':
                    ask_card = Card_library.Card(value_card, '♡')
                elif suit_card[0].lower() == 's' or suit_card == '♤':
                    ask_card = Card_library.Card(value_card, '♤')
                elif suit_card[0].lower() == 'c' or suit_card == '♧':
                    ask_card = Card_library.Card(value_card, '♧')
                elif suit_card[0].lower() == 'd' or suit_card == '♢':
                    ask_card = Card_library.Card(value_card, '♢')
                return ask_card
            except:
                print('Invalid option. Try Again')
                print('Ex: A of ♧ or A of spade')
              
        # if askplayer_card in self.player_hand:
        #     if askplayer_card in askplayer_player.player_hand:
        #         pass # PLACEHOLDER
        # else:
        #     pass # PLACEHOLDER

    def addToScore(self):
        score += 1
    
    def __str__(self):
        return "name: {} score: {}\n".format(self.name, self.score)


if __name__ == "__main__":
    p = Player('player 1')
    p.score = 4
    p.askForCard()
