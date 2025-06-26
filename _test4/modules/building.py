#spawn.py
import tkinter as tk

class Building:
    """
    """

    def __init__(self, root, factory, pos_x, pos_y, label_w, label_h, text=None):
        self.root = root
        self.factory = factory
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.label_w = label_w
        self.label_h = label_h
        self.text = text

        self.set_factory()

    def set_factory(self):
        label = tk.Label(self.root, )