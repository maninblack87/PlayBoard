# play_info/player.py

import tkinter as tk

class Player:

    def __init__(self, id, planeswalker=None, deck=None):
        self.id = id
        self.planeswalker = planeswalker    
        self.library = deck