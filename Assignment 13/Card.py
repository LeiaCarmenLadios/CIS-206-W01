import Deck as Deck_library

class Card:
    @property
    def card_value(self):
        """Gets/returns the VALUE"""
        return self._card_value

    @property
    def card_suit(self):
        """Gets/returns SUIT value"""
        return self._card_suit
    
    @property
    def card_file(self):
        """Gets/returns card URL value"""
        return self._card_file

    def __init__(self, card_value = None, card_suit = None, card_file = None):
        VALUE = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        SUIT = ['♧', '♢', '♡', '♤']
        if (card_value not in VALUE) or (card_suit not in SUIT):
            raise Exception('ERROR - Invalid card VALUE or SUIT')
        else:
            self._card_value = card_value
            self._card_suit = card_suit
            self._card_file = card_file

    def __str__(self):
        return "{} of {}".format(self.card_value, self.card_suit)


if __name__ == '__main__':
    crd = Card('A', 'F')
    print(crd)

    
