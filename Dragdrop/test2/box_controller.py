# box_controller.py
import tkinter as tk
from functools import partial
from config import ROOT, GRID
from dragdrop_label import DragDropLabel
from handle_drop import handle_drop

def create_box(master:tk.Widget, placed:tk.Widget):
    
    handle_drop_callback = partial(
        handle_drop,
        root = master,             
        x_cnt = GRID["count_x"],    
        y_cnt = GRID["count_y"],    
        grid_w = GRID["width"],      
        grid_h = GRID["height"],     
    )

    box = DragDropLabel(
        master, 
        text="Box", 
        bg="#ffffcc", 
        relief="raised",
        drop_callback = handle_drop_callback,
    )

    placed.master.update_idletasks() 
    create_place_x = placed.winfo_x() + placed.master.winfo_x()
    create_place_y = placed.winfo_y() + placed.master.winfo_y()
    box.place(
        x = create_place_x,
        y = create_place_y,
        width = 100,
        height = 100,
    )

    return box