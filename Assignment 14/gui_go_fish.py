import tkinter as tk
import go_fish as gf
import Card as Card_library
import Deck as Deck_library 
import Hand as Hand_library
import Player as Player_library
import Game as Game_library
from functools import partial

# https://stackoverflow.com/questions/26479728/tkinter-canvas-image-not-displaying    
# https://stackoverflow.com/questions/16424091/why-does-tkinter-image-not-show-up-if-created-in-a-function


class Root(tk.Tk):
    """Creates root window."""
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("GO FISH GAME")
        self.geometry("1200x800")


class MainMenu(tk.Menu):
    """Creates Main menu."""
    def __init__(self, root, *args, **kwargs):
        tk.Menu.__init__(self, root, *args, **kwargs)
        file_menu = FileMenu(self, tearoff=0)
        self.add_cascade(label="File", menu = file_menu)
        root.config(menu = self)

class FileMenu(tk.Menu):
    """Creates File menu."""
    def __init__(self, root, *args, **kwargs):
        tk.Menu.__init__(self, root, *args, **kwargs)
        make_new_game = partial(self.new_game, root)
        self.add_command(label="New Game", command= make_new_game)
        self.add_command(label="Exit", command=root.quit)

    def new_game(self,rt):
        root = Root()
        newMain = MainMenu(root)
        newCanvas = Canvas(root)
        rt.destroy()
        
       
class Canvas(tk.Canvas):
    """Creates drawing canvas."""

    def __init__(self, root, *args, **kwargs):
        tk.Canvas.__init__(self, root, *args, **kwargs)
        self.pack(fill="both", expand=True)
        self.game = Game_library.Game()
        self.display_start_page()
        self.images = []
        self.game_over = False
  
    def askNumPlayers(self, button1 = "", button2 = ""):
        self.clear_canvas()
        if(isinstance(button1, tk.Button)):
            button1.destroy()
        if(isinstance(button2, tk.Button)):
            button2.destroy()
        
        intro_msg = self.create_text(580, 275, font = ("Purisa", 18),
        text = """
        \t        Welcome to the game of GO FISH!!!\n
        # How many players will be playing? (minimum 2; maximum 5): """)
        global num_of_players 

        num_of_players= tk.IntVar()
        enter_num = tk.Entry(self, textvariable = num_of_players, font = ("Purisa", 13))
        enter_num.place(x=450, y =365, width = 200)
      
        submitNumPlayers_button = tk.Button(self, text ="Submit",  font = ("Purisa", 12), bg="light cyan")
        submitNumPlayers_button['command'] =  partial(self.validateNumPlayers, num_of_players, enter_num, submitNumPlayers_button)
        submitNumPlayers_button.pack(side="top")
        submitNumPlayers_button.place(x=655, y =360)
        

    def validateNumPlayers(self, num, entrybox, button):
        
        self.clear_canvas()
        button.place_forget()
        entrybox.place_forget()

        self.game.num_of_players = num.get()
        
        if self.game.num_of_players < 2:
            self.clear_canvas()
            playerName_msg = self.create_text(580, 250, font = ("Purisa", 12), fill = "red", text="You have entered less than the minimum(2) number of players.")
            self.askNumPlayers()
        elif self.game.num_of_players > 5:
            self.clear_canvas()
            playerName_msg = self.create_text(580, 250, font = ("Purisa", 12), fill = "red", text="You have entered more than the maximum(5) number of players.")
            self.askNumPlayers()
        else:
            self.get_names()

                
    def get_names(self):
        entered_names = []
        
        # playerNameAsk_msg = self.create_text(580, 250, font = ("Purisa", 12), text="Please enter player names: ")
        decoyLabel = tk.Label(self, text ="", pady = 120, bg = 'alice blue')
        decoyLabel.grid(row=0, column =0)

        playerNameAsk_msg = tk.Label(self, font = ("Purisa", 12), text = "Please enter player names: ", bg = 'alice blue')
        playerNameAsk_msg.grid(row = 1, column = 0)
        playerNameGiven = tk.StringVar()
       
        for x in range(self.game.num_of_players):
            enter_name = tk.Entry(self, font = ("Purisa", 12))
            enter_name.grid(row = x + 2, column = 0, padx = 525, pady = 10)
            entered_names.append(enter_name)

        submitPlayerName_button = tk.Button(self, text ="Submit", bg="light cyan") # lambda:[self.assignPlayerName(entered_names), submitPlayerName_button.destroy()]
        submitPlayerName_button['command'] = partial(self.assignPlayerName, entered_names, submitPlayerName_button)
        submitPlayerName_button.grid(row = self.game.num_of_players + 5, column = 0, pady =  20, padx =50)
        
    def assignPlayerName(self, playerNames, button = ""):
        if(isinstance(button, tk.Button)):
            button.destroy()
        for x in playerNames:
            self.game.addPlayers(x.get())

        for entryBox in self.grid_slaves():
            entryBox.grid_forget()

        print(self.game.print_player_list())
        self.clear_canvas()
        self.grid_forget()
        self.displayTurn()

            
    def displayTurn(self):  #https://pypi.org/project/unicards/ unicode characters for playing cards
        self.game.deal() 
        self.printCards()
        self.makeAskForPlayerName()
            

    def printCards(self, button1 = "", label = "", label2 = ""):
        print("Player name: ", self.game.current_player.name)
        self.clear_canvas()

        if(isinstance(button1, tk.Button)):
            button1.destroy()
            label.destroy()
            label2.destroy()
            self.makeAskForPlayerName()

        for player in self.game.player_list:
            self.game.checkFour(player)
        # self.game.checkFour(self.game.current_player)
        card_indent = 530 - (len(self.game.current_player.player_hand.hand_cards)*16)
        display_currentPlayer = self.create_text(570, 100, font = ("Purisa", 32), fill = "black", text= self.game.current_player.name + "'s turn.")
        display_currentPlayerScore = self.create_text(560, 210, font = ("Purisa", 22), fill = "black", text= "Score: " + str(self.game.current_player.score) + "\t\t\tBooks: " + str(self.game.current_player.books))
       
        i = 0
        while (i < len(self.game.current_player.player_hand.hand_cards)):
            print(self.game.current_player.player_hand.hand_cards[i].card_file)
            self.svgFile = tk.PhotoImage(file = "Assignment 14\\Cards2\\" + self.game.current_player.player_hand.hand_cards[i].card_file)
            self.svgFile = self.svgFile.subsample(2,2)
            self.create_image(card_indent , 300, anchor=tk.NW, image = self.svgFile)
            self.images.append(self.svgFile)
            card_indent += 37
            i += 1
            
    def remove_buttons(self, button_list):
        for button in button_list:
            button.destroy()
          
      
    def makeAskForPlayerName(self, text = ""):

        display_askOtherPlayerName = tk.Label(self, font = ("Purisa", 18), text ="Who would you like to ask for a card?", pady = 0, bg = 'alice blue')
        display_askOtherPlayerName.place(relx = 0.31, rely = 0.72)
        
        askPlayerButtonNames = []
        for player in self.game.player_list:
            if player.name not in self.game.current_player.name:
                askPlayerButtonNames.append(player.name)

        button_indent = 0.17
        button_refs = []
        for name in askPlayerButtonNames:
            button_indent += 0.13
            askPlayer_button = tk.Button(self, text = name, font = ("Purisa", 12), bg="light cyan") #command = lambda:[self.makeAskForCardPrompt(buttonValue), display_askOtherPlayerName.destroy(), self.remove_buttons(button_refs)])
            askPlayer_button['command'] = partial(self.makeAskForCardPrompt, name, button_refs, display_askOtherPlayerName, text)
            askPlayer_button.place(relx = button_indent, rely = 0.8)
            button_refs.append(askPlayer_button)
            
    
    def makeAskForCardPrompt(self, askedPlayerName, buttons, label, text =""):
        for player in self.game.player_list:
            if askedPlayerName == player.name:
                self.game.asked_player = player
                print(askedPlayerName + " " + player.name)
        label.place_forget()   
        self.remove_buttons(buttons)
        self.delete(text)

        print("Player asked: ", self.game.asked_player.name)

        display_askOtherPlayerCard = self.create_text(575, 600, font = ("Purisa", 18), fill = "black", text= "Which card would you like to ask for?")
        button_indent = 0.04
        existing_values = []
        for card in self.game.current_player.player_hand.hand_cards:
            if card.card_value not in existing_values:
                existing_values.append(card.card_value)

        button_ref = []
        for value in existing_values:
            button_indent += 0.040
            askCardValue_button = tk.Button(self, text = value, font = ("Purisa", 12), bg="light cyan") #lambda:[self.game.checkRequest(self.game.current_player, askedPlayer, crd), self.remove_buttons(button_refs)]
            buttonValue = askCardValue_button['text']
            crd = Card_library.Card(buttonValue, '♡')
            button_ref.append(askCardValue_button)
            askCardValue_button['command'] = partial(self.processCheckRequest, crd, askCardValue_button, button_ref, display_askOtherPlayerCard)
            askCardValue_button.place(relx = (0.25 + button_indent), rely = 0.8)

    def processCheckRequest(self, crd, button, button_list, text = ""):
        print("Card asked for: ", crd.card_value + crd.card_suit)
        button.place_forget()
        testRequest = self.game.checkRequest(self.game.asked_player, crd) #testing
        print(testRequest) #testing
        if(testRequest == True):
            self.clear_canvas()
            self.remove_buttons(button_list)
            self.printCards()
            display_askOtherPlayerCard = self.create_text(575, 558, font = ("Purisa", 16), fill = "black", text= "Correct! You received a new card. Go Again.")
            self.game.checkFour(self.game.current_player)

            if(len(self.game.player_list) <= 1):
                    """Game Ends"""
                    self.clear_canvas() 
                    end_game_msg = self.create_text(575, 558, font = ("Purisa", 16), fill = "black", text= "Winna!")
                        
            if len(self.game.current_player.player_hand.hand_cards) == 0:
                if(len(self.game.game_deck.deck_of_cards) == 0):
                    """Removing a player because no cards are left in the deck."""
                    self.game.finished_players.append(self.game.current_player)
                    x = self.game.player_list.index(self.game.current_player)
                    print("Player index:", x)
                    self.game.player_list.remove(self.game.current_player)

                    if(len(self.game.player_list) >= (x + 1)):
                        self.game.current_player = self.game.player_list[x]
                    else: 
                        self.game.current_player = self.game.player_list[0]

                    self.delete(display_askOtherPlayerCard)

                    for player in self.game.finished_players: #testing
                        print("Finished players:", player.name) #testing
                        
                    if(len(self.game.player_list) <= 1):
                        """Game Ends"""
                        self.clear_canvas() 
                        end_game_msg = self.create_text(575, 558, font = ("Purisa", 16), fill = "black", text= "Winna!")
                    else:
                        if(self.game.current_player not in self.game.finished_players):
                             self.printCards()
                             self.makeAskForPlayerName()
                else:
                    """Deals up to 5 cards depending on how many are left in the deck.
                        Then moves onto the next player and draws ask menu for next player.
                    """
                    for _ in range(5):
                        if (len(self.game.game_deck.deck_of_cards) > 0):
                            card = self.game.game_deck.draw()
                            self.game.current_player.player_hand.addToHand(card.card_value, card.card_suit, card.card_file)
                    self.game.nextPlayer()
                    self.printCards()
                    self.makeAskForPlayerName(display_askOtherPlayerCard)
            else:
                self.makeAskForPlayerName(display_askOtherPlayerCard)
        else:

            self.delete(text)
            self.remove_buttons(button_list)
          
            card = self.game.game_deck.draw()
            if(card is not None):
                self.game.current_player.player_hand.addToHand(card.card_value, card.card_suit, card.card_file)
                card_drawn_label = tk.Label(self, text = "You drew: ", font = ("Purisa", 16), bg = "alice blue")
                card_drawn_label.place(relx = 0.73, rely= 0.083)
                go_fish_label = tk.Label(self, text = "GO FISH!", font = ("Purisa", 42), bg = "alice blue", fg = "#008080")
                go_fish_label.place(relx = 0.39, rely= 0.64)
                self.svgFile = tk.PhotoImage(file = "Assignment 14\\Cards2\\" + card.card_file)
                self.svgFile = self.svgFile.subsample(2,2)
                self.create_image(1000, 70, anchor=tk.NW, image = self.svgFile)
            else: 
                card_drawn_label = tk.Label(self, text = "You drew: ", font = ("Purisa", 16), bg = "alice blue")
                card_drawn_label.place(relx = 0.73, rely= 0.083)
                go_fish_label = tk.Label(self, text = "GO FISH!", font = ("Purisa", 42), bg = "alice blue", fg = "#008080")
                go_fish_label.place(relx = 0.39, rely= 0.64)
                card_drawn_label['text'] = "Deck is empty"
           
            # print("False: ", card.card_file)
            self.game.nextPlayer()
            displayDrawnCards_button = tk.Button(self, text = "Next Player", font = ("Purisa", 12), bg="light cyan")
            displayDrawnCards_button.place(relx = 0.45, rely = 0.8)
            displayDrawnCards_button['command'] = partial(self.printCards, displayDrawnCards_button, card_drawn_label, go_fish_label)
            
            

        
            
           
    def display_start_page(self, button1 = ""):
        self.clear_canvas()
        
        if(isinstance(button1, tk.Button)):
            button1.destroy()
        
        startGame_button = tk.Button(self, text ="Start Game", font = ("Purisa", 14), bg="light cyan") #lambda:[self.clear_canvas(), self.askNumPlayers(), startGame_button.destroy(), gameRules_button.destroy()]
        startGame_button.pack(pady = (300, 20))
        gameRules_button = tk.Button(self, text ="Game Rules", font = ("Purisa", 14), bg="light cyan")
        gameRules_button.pack()
        startGame_button['command'] = partial(self.askNumPlayers, startGame_button, gameRules_button)
        gameRules_button['command'] = partial(self.display_game_rules, gameRules_button, startGame_button)
        
    def clear_canvas(self):
        self.delete("all")


    def display_game_rules(self, button1, button2):
        self.clear_canvas()
        button1.destroy()
        button2.destroy()
        self.create_text(580, 370, font=("Purisa", 13), 
        text=  """
        GAME RULES-
        
        1>  Each player is dealt five cards at the beginning of the game/  The remainder 
            of the pack is placed face down on the table to form the stock.

        2>  The first player whose name was entered first, goes first in the round of players. 

        3>  The player whose turn it is will be prompted to choose another player to ask a card from.

        4>  The player whose turnit is will then choose a card value they would like to ask that player for.

        5>  If the player has none, they say, "Go fish!" and the player who made the request draws the top card of the 
            deck and places it in their hand.
        
        6>  If a player gets one or more cards of the named rank that was asked for, they are entitled to ask the same or 
            another player for a card. The player can ask for the same card or a different one. So long as the player 
            succeeds in getting cards, their turn continues.

        7>  When a player makes a catch, they must reveal the card so that the catch is verified.
        
        8>  If a player gets the fourth card of a book, the player shows all four cards, places them on the table face up in 
            front of everyone, and plays again.

        9>  If the player goes fishing without "making a catch" (does not receive a card he asked for), 
            the turn passes to the left.

        10> During the game, if a player is left without cards, they may (when it's their turn to play), 
            draw from the stock and then ask for cards of that rank. If there are no cards left in the stock, 
            they are out of the game.

        11>The game ends when all thirteen books have been won. The winner is the player with the most books.""")

        back_button = tk.Button(self, text = "Back", bg="light cyan", font=("Purisa", 12))
        back_button.pack()
        back_button['command'] = partial(self.display_start_page, back_button)
        


if __name__ == "__main__":
    root = Root()
    menu = MainMenu(root)
    canvas = Canvas(root, bg = 'alice blue')
    root.resizable(width=False, height=False)
    root.mainloop()
