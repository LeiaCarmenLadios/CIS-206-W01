import tkinter as tk
import go_fish as gf
import Card as Card_library
import Deck as Deck_library 
import Hand as Hand_library
import Player as Player_library
import Game as Game_library

root = tk.Tk()
root.title("GO FISH!")

# Frames
main_frame = tk.Frame(root)
GameRules_frame = tk.Frame(root)
TheGame_frame = tk.Frame(root)



def new_game():
    main_frame.pack_forget()
    TheGame_frame.pack()
    # game = Game_library.Game()
    
    
def game_rules():
    main_frame.pack_forget()
    GameRules_frame.pack()
    # GameRules_frame.tkraise()

def show_main_frame():
    GameRules_frame.pack_forget()
    main_frame.pack()


description_1 = tk.Label(
    master=main_frame,
    text="Go Fish Game",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)

button_StartGame = tk.Button(
    master=main_frame,
    text="Start Game",
    #width=25,
    #height=3,
    #bg="blue",
    #fg="yellow",
    padx = 100, 
    pady= 10,
    command = new_game
)
#button_StartGame.grid(row = 0, column = 0)
button_StartGame.place(x = 336 , y = 325)
button_StartGame.pack()

button_GameRules = tk.Button(
    master=main_frame,
    text="Game Rules",
    #width=25,
    #height=3,
    #bg="blue",
    #fg="yellow",
    padx = 100,
    pady = 10,
    command = game_rules
)
# button_GameRules.grid(row = 1, column = 0)
button_GameRules.place(x = 335, y = 385)
button_GameRules.pack()

GameRules_label = tk.Label(
    master= GameRules_frame,
    text="""Rules:
    1>Any player deals one card face up to each player. The player with the lowest card is the dealer. The dealer shuffles the cards, and the player to the right cuts them.
    2>The dealer completes the cut and deals the cards clockwise one at a time, face down, beginning with the player to the left. Maximum number of players is 5 and everyone is dealt 5 cards each. The remainder of the pack is placed face down on the table to form the stock.
    3>The player to the left of the dealer looks directly at any opponent and says, for example, "Give me your kings," usually addressing the opponent by name and specifying the rank that they want, from ace down to two.
    4>The player who is "fishing “must have at least one card of the rank that was asked for in their hand. The player who is addressed must hand over all the cards requested.
    5>If the player has none, they say, "Go fish!" and the player who made the request draws the top card of the deck and places it in their hand.
    6>If a player gets one or more cards of the named rank that was asked for, they are entitled to ask the same or another player for a card. The player can ask for the same card or a different one. So long as the player succeeds in getting cards (makes a catch), their turn continues.
    7>When a player makes a catch, they must reveal the card so that the catch is verified.
    8>If a player gets the fourth card of a book, the player shows all four cards, places them on the table face up in front of everyone, and plays again.
    9>If the player goes fishing without "making a catch" (does not receive a card he asked for), the turn passes to the left.
    10>During the game, if a player is left without cards, they may (when it's their turn to play), draw from the stock and then ask for cards of that rank. If there are no cards left in the stock, they are out of the game.
    11>The game ends when all thirteen books have been won. The winner is the player with the most books.""",
    #foreground="white",  # Set the text color to white
    #background="black"  # Set the background color to black
)
GameRules_label.pack()

button_GameRules_back = tk.Button(
    master=GameRules_frame,
    text="Go Back",
    #width=25,
    #height=3,
    #bg="blue",
    #fg="yellow",
    padx = 100,
    pady = 10,
    command = show_main_frame
)
# button_GameRules.grid(row = 1, column = 0)
button_GameRules_back.pack()

main_frame.pack()

# button.grid(row = 0, column = 0)
# button_GameRules.grid(row = 1, column = 0)

# text_box = tk.Text(root, height = 4, width = 50)
# text_box.pack(side = tk.BOTTOM)

if __name__ == "__main__":
    
    root.mainloop()
