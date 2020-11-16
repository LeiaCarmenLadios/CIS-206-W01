import Card as Card_library
import Deck as Deck_library

class Hand:

    @property
    def hand_cards(self):
        return self._hand_cards
    
    @hand_cards.setter
    def hand_cards(self, hand):
        self._hand_cards = hand
    
    def __init__(self):           
        self.hand_cards = []

    def addToHand(self, value, suit):
        add_crd = Card_library.Card(value, suit)
        self.hand_cards.append(add_crd)

    def removeFromHand(self, value):
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
        print_hand = ''
        for crd in self.hand_cards:
            print_hand += "{} of {}\n".format(crd.card_value, crd.card_suit)
        return print_hand

if __name__ == "__main__":
    pass
