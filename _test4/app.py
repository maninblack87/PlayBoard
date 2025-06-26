# app.py
import tkinter as tk
from _test4.modules import tile

root = tk.Tk()
root.title("Sc 테스트4")
root.geometry("300x300")
root.resizable(False, False)
root.option_add("Font", "Gothic 12")

# 타일배치
map = tile.Tiling(root, 3, 3, 100, 100)

# 타일수정

root.mainloop()