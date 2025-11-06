# app.py
import tkinter as tk
import map


# 초기 설정
cols, rows = 5, 10
grid_w, grid_h = 150, 72


# 메인창
root = tk.Tk()
root.geometry(f"{cols*grid_w}x{rows*grid_h}+0+0")
root.title("테스트-mtg")
root.resizable(False, False)
root.option_add("Font", "Gothic 12")


# 매핑
mapping = map.Map(root, "frame", 0, 0, cols, rows, grid_w, grid_h)

# 유저1
user1_info = map.Map(root, "label", 0, 0, 2, 1, grid_w, grid_h)
user1_info.modify_bg(0, 0, 1, 1, "#faa")
#
mapping.modify_bg(0, 1, 1, 3, "#ffa")
#
user1_slots = map.Map(root, "frame", 0, 4, 1, 6, grid_w, grid_h)
user1_slots.modify_bg(0, 0, 1, 6, "#fee")


# 유저2
user2_info = map.Map(root, "label", cols-2, 0, 2, 1, grid_w, grid_h)
user2_info.modify_bg(1, 0, 1, 1, "#aaf")
#
mapping.modify_bg(cols-1, 1, 1, 3, "#aff")
#
user2_slots = map.Map(root, "frame", cols-1, 4, 1, 6, grid_w, grid_h)
user2_slots.modify_bg(0, 0, 1, 6, "#eef")

# GUI 실행
root.mainloop()