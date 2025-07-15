# planeswalkers/plnswkr_maker.py

import tkinter as tk
from .planeswalker import Planeswalker

root = tk.Tk()
root.title("테스트(생성)")
root.geometry("600x400+0+0")
root.option_add("Font", "Gothic 12")

grid_x, grid_y = 150, 50
cols, rows = 5, 7

name_lbl = tk.Label(root, text="레이블1", bg="lightgreen")
name_lbl.place(x=0, y=0, width=150, height=30)
name_ipt = tk.Entry(root)
name_ipt.place(x=170, y=3, width=200, height=24)

hitpoint_lbl = tk.Label(root, text="레이블2", bg="lightblue")


root.mainloop()