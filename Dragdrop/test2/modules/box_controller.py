# modules/box_controller.py
import tkinter as tk

class BoxController:

    def __init__(self, spawn_frame:tk.Frame):
        self.spawn_frame = spawn_frame
        self.boxs = {}