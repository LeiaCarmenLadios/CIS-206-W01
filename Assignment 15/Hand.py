import Card as Card_library
import Deck as Deck_library

class Hand:

    @property
    def hand_cards(self):
        """Gets/returns the cards in hand."""
        return self._hand_cards
    
    @hand_cards.setter
    def hand_cards(self, hand):
        """Sets the cards in the hand."""
        self._hand_cards = hand
    
    def __init__(self):    
        """Initialized hand cards to empty hand"""
        self.hand_cards = []

    def addToHand(self, value, suit, cfile):
        """Adds card object to hand list"""
        add_crd = Card_library.Card(value, suit, cfile)
        self.hand_cards.append(add_crd)

    def removeFromHand(self, value):
        """Removes all cards of the same value from hand"""
        # remove_crd = Card_library.Card(value, suit)     # QUESTION!!!!
        hand_length = len(self.hand_cards)
        i = 0
        while(i < (hand_length)):
            if (self.hand_cards[i].card_value == value):
                self.hand_cards.remove(self.hand_cards[i]) #be careful because the length of the list changes when you remove something
                i = 0                                             #THIS TOOK US TOO LONG LOL
                hand_length = len(self.hand_cards)
            else:
                i += 1

    def __str__(self):
        """__str__ magic method sets console output format for cards in hand"""
        print_hand = ''
        for crd in self.hand_cards:
            print_hand += "{} of {}\n".format(crd.card_value, crd.card_suit)
        return print_hand

if __name__ == "__main__":
    """Runs main program logic when current file is run as main"""
    pass
    

