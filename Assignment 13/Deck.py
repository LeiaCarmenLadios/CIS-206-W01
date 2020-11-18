import Card as Card_library
import random

class Deck:
    @property
    def deck_of_cards(self):
        return self._deck_of_cards

    def __init__(self):
        VALUE = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        SUIT = ['♧', '♢', '♡', '♤']
        self._deck_of_cards = []
        for s in SUIT:
            for v in VALUE:
                if s == '♧':
                    card_file = v + 'C' + '.svg'
                elif s == '♢':
                    card_file = v + 'D' + '.svg'
                elif s == '♡':
                    card_file = v + 'H' + '.svg'
                elif s == '♤':
                    card_file = v + 'S' + '.svg'
                crd = Card_library.Card(v, s, card_file)
                self._deck_of_cards.append(crd)

    def __str__(self):
        printString = ''
        for card in self._deck_of_cards:
            printString += "{} of {}\n".format(card.card_value, card.card_suit)
        return printString 

    def shuffle(self):
       return random.shuffle(self.deck_of_cards)

    def draw(self):
        if len(self.deck_of_cards) > 0:
            return self.deck_of_cards.pop()
        else:
            return None
        
    def reset(self):
        self.__init__()


if __name__ == "__main__":
    obj = Deck()
    print(obj)
    for card in obj.deck_of_cards:
        print("Card Value & Suit: " , card.card_value + card.card_suit)
        print("Card File Name: " , card.card_file, '\n')


   
