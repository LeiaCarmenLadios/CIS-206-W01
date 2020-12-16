import Deck as Deck_library

class Card:
    """Sets card values and prints them out."""
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
        """Checks card attributes in list for match (data validation).
            If matched, it will set the corresponding card data values. 
        
        Args:
            card_value (string): Value of the card.
            card_suit (string): Suit of the card.
            card_file (string): URL of the card image.

        Raises:
            Exception: If card_value or card_suit is not in the list.

        """
        VALUE = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        SUIT = ['♧', '♢', '♡', '♤']
        if (card_value not in VALUE) or (card_suit not in SUIT):
            raise Exception('ERROR - Invalid card VALUE or SUIT')
        else:
            self._card_value = card_value
            self._card_suit = card_suit
            self._card_file = card_file

    def __str__(self):
        """__str__ called when using print().
            Prints out card information in certain format.
        """
        return "{} of {}".format(self.card_value, self.card_suit)


if __name__ == '__main__':
    """Sets card values and prints them out."""
    crd = Card('A', '♧', 'AC.gif')
    print(crd)
