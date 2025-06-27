# app.py
import tkinter as tk
from modules import map, factory

root = tk.Tk()
root.title("Sc 테스트4")
root.geometry("300x300")
root.resizable(False, False)
root.option_add("Font", "Gothic 12")

x_length, y_length = 3, 3
map_w, map_h = 100, 100

# 타일 배치
map = map.Map(root, x_length, y_length, map_w, map_h)

# 타일 일부 수정
for y in range(y_length):
    for x in range(x_length):
        if x in [0, 2] and y in [0]:
            map.update_map(x, y, f"{x}, {y}", "yellowgreen")

# 팩토리 배치
for x in range(3):
    fac = factory.Factory(root, x, 2, 100, 100, f"팩토리{x+1}")

root.mainloop()