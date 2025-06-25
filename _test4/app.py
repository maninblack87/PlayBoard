# app.py
import tkinter as tk
from modules import tiling

root = tk.Tk()
root.title("Sc 테스트4")
root.geometry("300x300")
root.resizable(False, False)
root.option_add("Font", "Gothic 12")

# 타일배치
map = tiling.Tiling(root, 3, 3, 100, 100)

root.mainloop()