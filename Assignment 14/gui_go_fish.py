import tkinter as tk
import go_fish as gf
import Card as Card_library
import Deck as Deck_library 
import Hand as Hand_library
import Player as Player_library
import Game as Game_library
from functools import partial
# import PIL.Image
# import PIL.ImageTk

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
  
    def askNumPlayers(self):
       
        intro_msg = self.create_text(580, 300, font = ("Purisa", 18),
        text = """
        \t        Welcome to the game of GO FISH!!!\n
        # How many players will be playing? (minimum 2; maximum 5): """)
        global num_of_players 

        num_of_players= tk.IntVar()
        enter_num = tk.Entry(self, textvariable = num_of_players, font = ("Purisa", 13))
        enter_num.place(x=450, y =365, width = 200)
      

        submitNumPlayers_button = tk.Button(self, text ="Submit",  font = ("Purisa", 12), bg="light cyan", command = partial(self.validateNumPlayers, num_of_players, enter_num))
        
        submitNumPlayers_button.pack(side="top")
        submitNumPlayers_button.place(x=655, y =360)
        

    def validateNumPlayers(self, num, entrybox, button):
        
        self.clear_canvas()
        self.game.num_of_players = num.get()
        button.place_forget()
        entrybox.place_forget()
        
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
            # self.grid_rowconfigure(1, weight=2)
            # self.grid(row = 30, column = 9)
            enter_name.grid(row = x + 2, column = 0, padx = 525, pady = 10)
            entered_names.append(enter_name)
            
           

        submitPlayerName_button = tk.Button(self, text ="Submit", bg="light cyan", command = lambda:[self.assignPlayerName(entered_names), submitPlayerName_button.destroy()])
        submitPlayerName_button.grid(row = self.game.num_of_players + 5, column = 0, pady =  20, padx =50)
        
  
        # for _ in range(self.game.num_of_players):
            
        #     enter_name = tk.Entry(self, textvariable = playerNameGiven)
           
        #     enter_name.place(x=390, y = 350, width = 200)
        #    
            # submitPlayerName_button.wait_variable(playerNameGiven.get())
            
    def displayTurn(self):  #https://pypi.org/project/unicards/ unicode characters for playing cards
        self.game.deal()    
       
        # j = 0
        card_indent = 425
        display_currentPlayer = self.create_text(460, 225, font = ("Purisa", 18), fill = "black", text= self.game.current_player.name + "'s turn.")
        display_currentPlayerScore = self.create_text(660, 225, font = ("Purisa", 18), fill = "black", text= "Book Count: " + str(self.game.current_player.score))
       
        i = 0
        while (i < len(self.game.current_player.player_hand.hand_cards)):
            print(self.game.current_player.player_hand.hand_cards[i].card_file)
            self.svgFile = tk.PhotoImage(file = "Assignment 14\\Cards2\\" + self.game.current_player.player_hand.hand_cards[i].card_file)
            self.svgFile = self.svgFile.subsample(2,2)
            self.create_image(card_indent , 300, anchor=tk.NW, image = self.svgFile)
            self.images.append(self.svgFile)
            card_indent +=50
            i += 1
        
        display_askOtherPlayerName = tk.Label(self, font = ("Purisa", 18), text ="Who would you like to ask for a card?", pady = 0, bg = 'alice blue')
        display_askOtherPlayerName.place(relx = 0.31, rely = 0.72)

        askPlayerButtonNames = []
        for player in self.game.player_list:
            if player.name not in self.game.current_player.name:
                askPlayerButtonNames.append(player.name)

        button_indent = 0.08
        button_refs = []
        for name in askPlayerButtonNames:
            button_indent += 0.2
            askPlayer_button = tk.Button(self, text = name, bg="light cyan", command = lambda:[self.askPlayerForCard(name), display_askOtherPlayerName.destroy(), self.remove_buttons(button_refs)])
            askPlayer_button.place(relx = button_indent, rely = 0.8)
            button_refs.append(askPlayer_button)
            

    def remove_buttons(self, button_list):
        for button in button_list:
            button.destroy()
            
    def askPlayerForCard(self, askedPlayerName):
        askedPlayer = Player_library.Player()
        
        for player in self.game.player_list:
            if askedPlayerName in player.name:
                askedPlayer = player

        display_askOtherPlayerCard = self.create_text(575, 600, font = ("Purisa", 18), fill = "black", text= "Which card would you like to ask for?")
            
        button_indent = 0.05
        button_refs = []
        existing_values = []
        for card in self.game.current_player.player_hand.hand_cards:
            if card.card_value not in existing_values:
                existing_values.append(card.card_value)

        for value in existing_values:
            button_indent += 0.16
            askCardValue_button = tk.Button(self, text = value, bg="light cyan", command = lambda:[self.game.checkRequest(self.game.current_player, askedPlayer, crd), self.remove_buttons(button_refs)])
            buttonValue = askCardValue_button['text']
            crd = Card_library.Card(buttonValue, '♡')
            askCardValue_button.place(relx = button_indent, rely = 0.8)
            button_refs.append(askCardValue_button)
    

    # def add_image(self, player_index, hand_index, card_indent):

    #     pathBuilder = "CIS-143-W01\\Assignment 12\\Cards2\\"+ self.game.player_list[player_index].player_hand.hand_cards[hand_index].card_file
    #     self.svgFile = tk.PhotoImage(file = pathBuilder)
    #     self.svgFile = self.svgFile.subsample(3,3)
    #     self.create_image(card_indent, 20, anchor=tk.NW, image = self.svgFile)

    def assignPlayerName(self, playerNames):
        for x in playerNames:
            self.game.addPlayers(x.get())

        for entryBox in self.grid_slaves():
            entryBox.grid_forget()

        print(self.game.print_player_list())
        self.clear_canvas()
        self.grid_forget()
        self.displayTurn()
       
    def display_start_page(self):
        startGame_button = tk.Button(self, text ="Start Game", font = ("Purisa", 14), bg="light cyan", command =lambda:[self.clear_canvas(), self.askNumPlayers(), startGame_button.destroy(), gameRules_button.destroy()])
        startGame_button.pack(pady = (300, 20))
        gameRules_button = tk.Button(self, text ="Game Rules", font = ("Purisa", 14), bg="light cyan", command =lambda:[self.clear_canvas(), self.display_game_rules(), gameRules_button.destroy(), startGame_button.destroy()] )
        gameRules_button.pack()
        
    def clear_canvas(self):
        self.delete("all")
        
    def retrieve_canvas(self):
        self.clear_canvas()

    def display_game_rules(self):
        self.create_text(580, 350, font=("Purisa", 12), 
        text=  """
        GAME RULES-
        
        1>  Any player deals one card face up to each player. The player with the lowest card is the dealer. 
            The dealer shuffles the cards, and the player to the right cuts them.

        2>  The dealer completes the cut and deals the cards clockwise one at a time, face down, beginning with 
            the player to the left. Maximum number of players is 5 and everyone is dealt 5 cards each. The remainder 
            of the pack is placed face down on the table to form the stock.

        3>  The player to the left of the dealer looks directly at any opponent and says, for example, "Give me your 
            kings," usually addressing the opponent by name and specifying the rank that they want, from ace down to two.

        4>  The player who is "fishing “must have at least one card of the rank that was asked for in their hand. The 
            player who is addressed must hand over all the cards requested.

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

        back_button = tk.Button(self, text = "Back", bg="light cyan", command = lambda:[self.retrieve_canvas(), back_button.destroy(), self.display_start_page()])
        back_button.pack()
        

        
        


# root = tk.Tk()
# root.title("GO FISH!")

# # Frames
# main_frame = tk.Frame(root)
# GameRules_frame = tk.Frame(root)
# TheGame_frame = tk.Frame(root)


    
# def game_rules():
#     main_frame.pack_forget()
#     GameRules_frame.pack()
#     # GameRules_frame.tkraise()

# def show_main_frame():
#     GameRules_frame.pack_forget()
#     main_frame.pack()


# description_1 = tk.Label(
#     master=main_frame,
#     text="Go Fish Game",
#     foreground="white",  # Set the text color to white
#     background="black"  # Set the background color to black
# )

# button_StartGame = tk.Button(
#     master=main_frame,
#     text="Start Game",
#     #width=25,
#     #height=3,
#     #bg="blue",
#     #fg="yellow",
#     padx = 100, 
#     pady= 10,
#     command = new_game
# )
# #button_StartGame.grid(row = 0, column = 0)
# button_StartGame.place(x = 336 , y = 325)
# button_StartGame.pack()

# button_GameRules = tk.Button(
#     master=main_frame,
#     text="Game Rules",
#     #width=25,
#     #height=3,
#     #bg="blue",
#     #fg="yellow",
#     padx = 100,
#     pady = 10,
#     command = game_rules
# )
# # button_GameRules.grid(row = 1, column = 0)
# button_GameRules.place(x = 335, y = 385)
# button_GameRules.pack()



# button_GameRules_back = tk.Button(
#     master=GameRules_frame,
#     text="Go Back",
#     #width=25,
#     #height=3,
#     #bg="blue",
#     #fg="yellow",
#     padx = 100,
#     pady = 10,
#     command = show_main_frame
# )
# # button_GameRules.grid(row = 1, column = 0)
# button_GameRules_back.pack()

# main_frame.pack()

# # button.grid(row = 0, column = 0)
# # button_GameRules.grid(row = 1, column = 0)

# # text_box = tk.Text(root, height = 4, width = 50)
# # text_box.pack(side = tk.BOTTOM)

if __name__ == "__main__":
    root = Root()
    menu = MainMenu(root)
    canvas = Canvas(root, bg = 'alice blue')
    

    root.mainloop()
