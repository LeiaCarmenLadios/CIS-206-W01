import Hand as Hand_library
import Card as Card_library
import Deck as Deck_library
import sys

class Player:

    @property # allows us to access the method like it's a property
    def name(self):
        """Gets/returns the player name."""
        return self._name

    @name.setter 
    def name(self, name):
        """Sets the name of player."""
        self._name = name

    @property 
    def is_playing(self):
        """Gets/returns bool indicating whether player is playing."""
        return self._is_playing

    @is_playing.setter
    def is_playing(self, is_playing):
        """Sets bool indicating whether player is playing."""
        self._is_playing = is_playing

    @property 
    def score(self):
        """Gets/returns score (number of books)."""
        return self._score
    
    @score.setter
    def score(self, score):
        """Sets player score."""
        self._score = score

    @property 
    def player_hand(self):
        """Gets/returns player hand."""
        return self._player_hand

    @property 
    def books(self):
        """Gets/returns books (list of cards won that determine score)."""
        return self._books

    def __init__(self, name = "Player"):
        """Initializes Player instance object with data attributes."""
        self.name = name
        self.is_playing = False
        self.score = 0
        self._books = []
        self._player_hand = Hand_library.Hand()

    def askForCard(self):
        """Prompts user for which card they would like to ask for and takes input."""
        VALUE = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        while True:
            print(self.player_hand)
            value_card = input("Which card value you like to ask for? [card value]: ") # string
            if value_card == "Quit" or value_card == "quit":
                sys.exit(0)  
                # if value_card.isalpha():
                #     value_card = value_card[0].upper()
                # if suit_card[0].lower() == 'h' or suit_card == '♡':
                #     ask_card = Card_library.Card(value_card, '♡')
                # elif suit_card[0].lower() == 's' or suit_card == '♤':
                #     ask_card = Card_library.Card(value_card, '♤')
                # elif suit_card[0].lower() == 'c' or suit_card == '♧':
                #     ask_card = Card_library.Card(value_card, '♧')
                # elif suit_card[0].lower() == 'd' or suit_card == '♢':
                #     ask_card = Card_library.Card(value_card, '♢')
            value_card = value_card.upper()
            if value_card in VALUE:
                ask_card = Card_library.Card(value_card, '♡')
                return ask_card
            else:
                print("\nInvalid card value. Please try again.\n")
                print("Please enter a character. Ex: For Ace, enter \'A\'.")
            
              
        # if askplayer_card in self.player_hand:
        #     if askplayer_card in askplayer_player.player_hand:
        #         pass # PLACEHOLDER
        # else:
        #     pass # PLACEHOLDER 

    def addToScore(self):
        """Adds 1 point to player score"""
        self.score += 1
    
    def __str__(self):
        """__str__ magic method that formats console output for Player objects"""
        return "\nName: {} Score: {} Books: {}".format(self.name, self.score, self.books)


if __name__ == "__main__":
    """Runs main program logic when current file is run as main"""
    pass
