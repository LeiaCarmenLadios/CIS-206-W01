class Card:
    card_value = None
    card_suit = None
    
    def __init__(self, card_value = None, card_suit = None):
        self.card_value = card_value
        self.card_suit = card_suit

    # @property
    # def card_value(self):
    #     """Gets/returns the VALUE"""
    #     return self._card_value


    # @property
    # def card_suit(self):
    #     """Gets/returns SUIT value"""
    #     return self._card_suit


