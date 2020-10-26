import Hand as Hand_library
import Card
import Deck

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
        print(self.player_hand)
        askplayer_card = input("which card would you like to ask for? [card value]: ") # string 
        value_card,suit_card = askplayer_card.split(' of ')

        print(suit_card)
        ask_card = Card()
        if suit_card == 'Hearts':
            ask_card = Card(value_card, '♡')
        elif suit_card == 'Spades':
            ask_card = Card(value_card, '♤')
        elif suit_card == 'Clubs':
            ask_card = Card(value_card, '♧')
        elif suit_card == 'Diamonds':
            ask_card = Card(value_card, '♢')
        else:
            print('Invalid option. Try Again')
        
        return ask_card
        # if askplayer_card in self.player_hand:
        #     if askplayer_card in askplayer_player.player_hand:
        #         pass # PLACEHOLDER
        # else:
        #     pass # PLACEHOLDER

    def __str__(self):
        return "name: {} score: {}\n".format(self.name, self.score)

# p = Player('player 1')
# p.score = 4
# p.askPlayer()



        
