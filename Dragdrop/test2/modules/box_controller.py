# modules/box_controller.py
import tkinter as tk

class BoxController:

    def __init__(self, master, box_slot:tk.Frame, create_box_btn:tk.Button, delete_box_btn:tk.Button, box_width:int, box_height:int):
        self.master = master
        self.box_slot = box_slot
        self.create_box_btn = create_box_btn
        self.delete_box_btn = delete_box_btn

        self.boxs = {}
        self.box_width = box_width
        self.box_height = box_height

    def create_box(self, event):
        box = tk.Label(self.master, text="Box", width=self.box_width, height=self.box_height)
        box.place(
            x = self.box_slot.winfo_x,
            y = self.box_slot.winfo_y,
        )