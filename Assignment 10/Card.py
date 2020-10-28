class Card:
    @property
    def card_value(self):
        """Gets/returns the VALUE"""
        return self._card_value

    @property
    def card_suit(self):
        """Gets/returns SUIT value"""
        return self._card_suit

    
    def __init__(self, card_value = None, card_suit = None):
        self._card_value = card_value
        self._card_suit = card_suit

    def __str__(self):
        return "{} of {}".format(self.card_value, self.card_suit)
