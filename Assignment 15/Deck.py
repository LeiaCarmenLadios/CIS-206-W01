import Card as Card_library
import random

class Deck:
    """Creates a deck of cards."""
    @property
    def deck_of_cards(self):
        """Gets/returns the whole deck."""
        return self._deck_of_cards

    def __init__(self):
        """Constructs the deck and creates each individual card with
            value, suit, and picutre attributes. 
        
        Args:
            None.

        Raises:
            None.

        """
        VALUE = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        SUIT = ['♧', '♢', '♡', '♤']
        self._deck_of_cards = []
        for s in SUIT:
            for v in VALUE:
                if s == '♧':
                    card_file = v + 'C' + '.gif'
                elif s == '♢':
                    card_file = v + 'D' + '.gif'
                elif s == '♡':
                    card_file = v + 'H' + '.gif'
                elif s == '♤':
                    card_file = v + 'S' + '.gif'
                crd = Card_library.Card(v, s, card_file) #Has no card member???
                self._deck_of_cards.append(crd)

    def __str__(self):
        """__str__ called when using print().
            Prints out card information in certain format.
        """
        printString = ''
        for card in self._deck_of_cards:
            printString += "{} of {}\n".format(card.card_value, card.card_suit)
        return printString 

    def shuffle(self):
        """Shuffles the deck."""
        return random.shuffle(self.deck_of_cards)

    def draw(self):
        """Returns a card and deletes it from the deck when the player draws.
            Checks if the deck is empty.
        """
        if len(self.deck_of_cards) > 0:
            return self.deck_of_cards.pop()
        else:
            return None

    def reset(self):
        """Runs the init function again. Constructs a new deck."""
        self.__init__()

if __name__ == "__main__":
    """Initializes deck class (creates a new deck), then prints out information on all cards in deck."""
    obj = Deck()
    print(obj)
    for card in obj.deck_of_cards:
        print("Card Value & Suit: " , card.card_value + card.card_suit)
        print("Card File Name: " , card.card_file, '\n')
