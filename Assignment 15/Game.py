"""Contains functions related to interactions between players (4-of-a-kind, scoring,
    asking another player for a card, dealing...)

Input:
    None ### should things outside of init be included?

Output:
    WIP

Notes:
    WIP

References:
    WIP
"""

import Card as Card_library
import Deck as Deck_library 
import Hand as Hand_library
import Player as Player_library

class Game:
    @property
    def game_deck(self):
        """Gets/returns the local deck."""
        return self._game_deck

    @property 
    def player_list(self):
        """Gets/returns the player list."""
        return self._player_list

    @property 
    def finished_players(self):
        """Gets/returns the list of players that finished the current game."""
        return self._finished_players

    @property 
    def num_of_players(self):
        """Gets/returns the total number of players."""
        return self._num_of_players

    @property
    def current_player(self):
        """Gets/returns the name of the current player."""
        return self._current_player

    @num_of_players.setter
    def num_of_players(self, num):
        """Sets the number of current player."""
        self._num_of_players = num

    @property
    def asked_player(self):
        """Gets/returns the name of the player being asked for a card."""
        return self._asked_player

    @asked_player.setter
    def asked_player(self, name):
        """Sets the name of player being asked for a card."""
        self._asked_player = name

    @property
    def current_player_index(self):
        """Gets/returns the index of the current player in the list."""
        return self._current_player_index

    @current_player.setter
    def current_player(self, player):
        """Sets the name of the current player."""
        self._current_player = player

    @current_player_index.setter
    def current_player_index(self, index):
        """Sets the index of the current player in the list."""
        self._current_player_index = index

    def __init__(self):
        """Initialized needed variables."""
        self._current_player = Player_library.Player()
        self._game_deck = Deck_library.Deck()
        self._player_list = []
        self._finished_players = []
        self.num_of_players = len(self.player_list)
        self.asked_player = Player_library.Player()
        self._current_player_index = 0

    def addPlayers(self, playerName):
        """Adds a player to the player_list."""
        player_to_add = Player_library.Player(playerName)
        self.player_list.append(player_to_add)
        self._current_player = self.player_list[0]
        self._current_player_index = 0

    def nextPlayer(self):
        """Adds one to player_index, changing the index of the current player in the list."""
        self.current_player_index = (self.current_player_index + 1) % (len(self.player_list))
        self.current_player = self.player_list[(self.current_player_index)]

    def print_player_list(self):
        """Prints out player list."""
        name_list = 'Players: ('
        for player in self.player_list:
            name_list += player.name + ", "
        name_list = name_list[:-2]
        return name_list + ')'

    def deal(self):
        """Deals 5 cards to each player."""
        self._game_deck.shuffle()
        counter = 5
        while(counter != 0):
            for player in self.player_list:
                card_deal = self.game_deck.deck_of_cards[len(self.game_deck.deck_of_cards)-1]
                self.game_deck.draw()
                player.player_hand.addToHand(card_deal.card_value, card_deal.card_suit, card_deal.card_file)
            counter -= 1

    def checkFour(self, player):
        """Checks for a match of 4 cards of the same value, then removes them
            if found and adds to the corresponding player's score.
        """ ###
        # crd = Card_library.Card('A', '♢')
        # player.player_hand.addToHand(crd.card_value, crd.card_suit)
        # crd2 = Card_library.Card('A', '♤')
        # player.player_hand.addToHand(crd2.card_value, crd2.card_suit)
        # crd3 = Card_library.Card('2', '♡')
        # player.player_hand.addToHand(crd3.card_value, crd3.card_suit)
        # crd4 = Card_library.Card('A', '♧')
        # player.player_hand.addToHand(crd4.card_value, crd4.card_suit)
        # crd5 = Card_library.Card('A', '♡')
        # player.player_hand.addToHand(crd5.card_value, crd5.card_suit)
        player_hand_list = []
        for ix in range(len(player.player_hand.hand_cards)):
            player_hand_list.append(player.player_hand.hand_cards[ix].card_value)
        player_hand_list.sort()
        # print(player_hand_list)
        to_remove = []
        counter = 1
        something = len(player_hand_list)
        for i in range(something):
            check_card = player_hand_list[i]
            if (i+1) < (len(player_hand_list)):
                if player_hand_list[i+1] == check_card: 
                    counter += 1
                else:
                    counter = 1
                if counter == 4:
                    to_remove.append(check_card)
                    counter = 0
        for ix in to_remove:
            player.addToScore()
            player.books.append(ix)
            player.player_hand.removeFromHand(ix)

    def checkRequest(self, player_asked, card):
        """When a player asks another player for a card, checks for that card, then
            transfers the card if found.
        """
        is_found = False
        suits_to_transfer = []
        for crd in player_asked.player_hand.hand_cards:
            if crd.card_value == card.card_value:
                suits_to_transfer.append(crd.card_suit)
                is_found = True
                print("card is found:", crd.card_value)
        for suit in suits_to_transfer:
            player_asked.player_hand.removeFromHand(card.card_value)
            file_string = ""
            if suit == '♧':
                file_string = card.card_value + 'C' + ".gif"
            elif suit == '♢':
                file_string = card.card_value + 'D' + ".gif"
            elif suit == '♡':
                file_string = card.card_value + 'H' + ".gif"
            elif suit == '♤':
                file_string = card.card_value + 'S' + ".gif"
            self.current_player.player_hand.addToHand(card.card_value, suit, file_string)
        return is_found

    def askAnotherPlayer(self, current_player_obj, card_needed):
        """Allows the player to input the name of the player they want to ask for a card,
            and validates to make sure that the name is valid.
        """
        is_found = False
        print("\nWho would you like to ask a card from?")
        print(self.print_player_list())
        name_of_player = input()
        player_asked_for = Player_library.Player()
        print(player_asked_for.player_hand)
        for plyr in self.player_list:
            if plyr.name.lower() == name_of_player.lower():
                player_asked_for = plyr
        if name_of_player.lower() == player_asked_for.name.lower():
            is_found = self.checkRequest(current_player_obj, player_asked_for, card_needed)
        else:
            print("There is no player with that name. Please try again.")  
        return is_found        

if __name__ == "__main__":
    pass 
