import Hand as Hand_library
import Card
import Deck

class Player:
    name = "Player"
    hand = Hand_library.Hand()
    is_playing = false
    score = 0
    books = []
    
    def __init__(self, name):
        self.name = name
