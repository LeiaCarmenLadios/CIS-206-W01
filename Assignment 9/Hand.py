import Card as Card_library
import Deck as Deck_library

class Hand:
    player_hand = []

    def __init__(self):             # for testing only
        test_crd = Card_library.Card('A', '♧')
        self.player_hand = [test_crd]

    def addToHand(self, value, suit):
        add_crd = Card_library.Card(value, suit)
        self.player_hand.append(add_crd)

    def removeFromHand(self, value, suit):
        remove_crd = Card_library.Card(value, suit)
        for crd in self.player_hand:
            if(crd.card_value == value):
                self.player_hand.remove(remove_crd)
            
    def print_hand(self):
        for crd in self.player_hand:
            print(crd)
        
