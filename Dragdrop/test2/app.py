# app.py
import tkinter as tk
from config import ROOT_HEIGHT, ROOT_WIDTH, MAP_HEIGHT, MAP_WIDTH, MAP_X, MAP_Y
from modules.handle_drop import handle_drop

# root 메인 창
root = tk.Tk()
root.title("드래그 드롭 테스트2")
root.geometry(f"{ROOT_WIDTH}x{ROOT_HEIGHT}+0+0")
root.resizable(False, False)

# 맵
map_frames = {}
for y in range(MAP_Y):
    for x in range(MAP_X):
        map_frame = tk.Frame(root, relief="solid", borderwidth=1)
        map_frame.place(
            x = x * MAP_WIDTH,
            y = y * MAP_HEIGHT,
            width = MAP_WIDTH,
            height = MAP_HEIGHT,
        )
        map_frames[(x, y)] = map_frame

# 컨트롤 프레임
ctrl_frame = tk.Frame(root, padx=20)
ctrl_frame.place(
    x = 0,
    y = MAP_Y * MAP_HEIGHT,
    width = ROOT_WIDTH,
    height = ROOT_HEIGHT - (MAP_Y * MAP_HEIGHT)
)
# >> 레이블 조작 버튼(생성, 삭제 등)
create_box_btn = tk.Button(ctrl_frame, text="박스생성", padx=10, pady=10)
create_box_btn.pack(side="left", padx=20)
delete_box_btn = tk.Button(ctrl_frame, text="박스삭제", padx=10, pady=10)
delete_box_btn.pack(side="left", padx=20)
# >> 박스 스폰 위치
box_slot = tk.Frame(ctrl_frame, width=100, height=100, relief="sunken", borderwidth=2)
box_slot.pack(side="left", padx=20)

# GUI 활성화
root.mainloop()