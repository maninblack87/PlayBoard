# app.py
import tkinter as tk

from config import ROOT, MAP
from box_controller import create_box

# 메인 창
root = tk.Tk()
root.title("DragDrop")
root.geometry(f"{ROOT["width"]}x{ROOT["height"]}")
root.resizable(False, False)
root.option_add("Font", "Gothic 12")

# 맵 프레임
map_frame = tk.Frame(root, bg="#ffcccc", width=800, height=600)
map_frame.pack(side="top")
# 맵
maps = {}
for y in range(MAP["y"]):
    for x in range(MAP["x"]):
        map = tk.Frame(map_frame, borderwidth=1, relief="solid")
        map.place(
            x = x * MAP["width"],
            y = y * MAP["height"],
            width = MAP["width"],
            height = MAP["height"],
        )
        maps[(x, y)] = map

# 컨트롤 프레임
ctrl_frame = tk.Frame(root, bg="#2b2b2b", width=800, height=150, padx=20, pady=20)
ctrl_frame.pack(side="top", fill="both")
# 박스 생성 버튼
create_box_btn = tk.Button(ctrl_frame, text="박스생성", padx=10, pady=10, command=lambda: create_box(root, maps[(0, 1)]))
create_box_btn.pack(side="left", padx=20)
# 나가기 버튼
quit_btn = tk.Button(ctrl_frame, text="나가기", padx=10, pady=10, command=root.quit)
quit_btn.pack(side="left", padx=20)

# GUI 활성화
root.mainloop()