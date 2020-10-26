class Card:
    def __init__(self, card_value = None, card_suit = None):
        self.card_value = card_value
        self.card_suit = card_suit

    def __str__(self):
        return "{} of {}".format(self.card_value, self.card_suit)