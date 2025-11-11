# box_controller.py
import tkinter as tk

def create_box(master:tk.Widget, placed:tk.Widget):
    box = tk.Label(master, bg="#00ccff", text="Test")
    box.place(
        x = placed.winfo_x(),
        y = placed.winfo_y(),
        width = 100,
        height = 100,
    )