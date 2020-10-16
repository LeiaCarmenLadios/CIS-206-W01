import Card as Card_library
import random

class Deck:
    size = 52
    deck_of_cards = []
    
    def __init__(self):
        VALUE = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K']
        SUIT = ['C', 'D', 'H', 'S']
        for s in SUIT:
            for v in VALUE:
                crd = Card_library.Card(v, s)
                self.deck_of_cards.append(crd)

    def shuffle(self):
       random.shuffle(self.deck_of_cards)

    def draw(self):
        return self.deck_of_cards.pop()

    def reset(self):
        self.__init__()



# obj = Deck()
# for c in obj.deck_of_cards:   
#     print(c.card_suit + c.card_value)
# print("\n")
# obj.shuffle()
# for c in obj.deck_of_cards:   
#     print(c.card_suit + c.card_value)
# obj.reset()
# for c in obj.deck_of_cards:   
#     print(c.card_suit + c.card_value)


