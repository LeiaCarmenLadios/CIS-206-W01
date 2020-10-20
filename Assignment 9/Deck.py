import Card as Card_library
import random

class Deck:
    deck_of_cards = []
    
    def __init__(self):
        VALUE = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        SUIT = ['♧', '♢', '♡', '♤']
        for s in SUIT:
            for v in VALUE:
                crd = Card_library.Card(v, s)
                self.deck_of_cards.append(crd)

    def print_deck(self):
        for card in self.deck_of_cards:
            print(card)

    def shuffle(self):
       random.shuffle(self.deck_of_cards)

    def draw(self):
        return self.deck_of_cards.pop()

    def reset(self):
        self.__init__()



# obj = Deck()
# for c in obj.deck_of_cards:   
#     print(c.card_value + c.card_suit)
# obj.print_deck()
# print("\n")
# obj.shuffle()
# for c in obj.deck_of_cards:   
#     print(c.card_suit + c.card_value)
# obj.reset()
# for c in obj.deck_of_cards:   
#     print(c.card_suit + c.card_value)


