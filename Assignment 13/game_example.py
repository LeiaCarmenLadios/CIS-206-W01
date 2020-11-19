# Game Example
from tkinter import *
from tkinter import ttk

def all_children(window):
    _list = window.winfo_children()
    for item in _list:
        if item.winfo_children():
            _list.extend(item.winfo_children())
    return _list

# specific to class?
def clear_screen(class_name):
    widget_list = all_children(class_name.mainframe)
    for item in widget_list:
        item.grid_forget()

class MainMenu:
    def __init__(self, root):
        root.title("Go Fish") # Gives title
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ttk.Button(
            mainframe,
            text="Start Game",
            command=self.start_game_command,
            ).grid(column=3, row=3, sticky=W)

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

    def start_game_command(self):
        clear_screen('MainMenu')

root = Tk() # Sets up the main application window
MainMenu(root)
root.mainloop() # necessary for tkinter