# app.py
import tkinter as tk
from functools import partial

from config import ROOT_WIDTH, ROOT_HEIGHT, MAP_WIDTH, MAP_HEIGHT, MAP_X, MAP_Y
from dragdrop_label import DragDropLabel
from handle_drop import handle_drop

# 메인 창
root = tk.Tk()
root.title("DragDrop")
root.geometry(f"{ROOT_WIDTH}x{ROOT_HEIGHT}")
root.resizable(False, False)
root.option_add("Font", "Gothic 12")

# 맵핑
map_frames = {}
for y in range(MAP_Y):
    for x in range(MAP_X):
        map_frame = tk.Frame(root, borderwidth=1, relief="solid")
        map_frame.place(
            x = x * MAP_WIDTH,
            y = y * MAP_HEIGHT,
            width = MAP_WIDTH,
            height = MAP_HEIGHT,
        )
        map_frames[(x, y)] = map_frame

handle_drop_callback = partial(handle_drop, root, map_frames, map_width=MAP_WIDTH, map_height=MAP_HEIGHT)

# << 테스트용 레이블 >>
test_lbl = DragDropLabel(root, handle_drop_callback, relief="raised", text="테스트\n레이블")
test_lbl.place(
    x = 0,
    y = 0,
    width = MAP_WIDTH,
    height = MAP_HEIGHT,
)

# GUI 활성화
root.mainloop()