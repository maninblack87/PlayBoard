# app.py
import tkinter as tk
import map, factory

root = tk.Tk()
root.title("Sc 테스트4")
root.geometry("400x400")
root.resizable(False, False)
root.option_add("Font", "Gothic 12")

x_length, y_length = 4, 4
map_w, map_h = 100, 100

# 맵 배치
map = map.Map(root, x_length, y_length, map_w, map_h)

# 맵 일부 요소(타일) 수정
for y in range(y_length):
    for x in range(x_length):
        if x in [0, 3] and y in [0]:
            map.modify_map(x, y, f"{x}, {y}", "yellowgreen")

# 팩토리 배치
fac_w, fac_h = 90, 90
i = 0
for y in range(y_length):
    for x in range(x_length):
        if x in [0, 1] and y in [2,3]:
            i = i + 1
            fac = factory.Factory(root, map_w, map_h, x, y, fac_w, fac_h, f"팩토리{i}")

root.mainloop()