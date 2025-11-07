# modules/handle_drop.py
import tkinter as tk
from dragdrop_label import DragDropLabel

def handle_drop(root:tk.Tk|tk.Widget, drop_label:tk.Label|DragDropLabel, map_frames:dict , map_width, map_height):

    # 드롭된 레이블(이하 레이블)의 그리드 상의 위치 값을 산출한다
    # 1. 메인 창 내에서 마우스 커서의 위치
    mouse_x_in_root = drop_label.winfo_pointerx() - root.winfo_x()
    mouse_y_in_root = drop_label.winfo_pointery() - root.winfo_y()
    # 2. 그리드 상의 위치
    grid_x = mouse_x_in_root // map_width
    grid_y = mouse_y_in_root // map_height
    
    # 만약 대상 프레임(들) 영역 내에 마우스 커서를 위치 시키면
    # >> 해당 레이블의 위치를 그리드 상으로 이동시킨다
    if (grid_x, grid_y) in map_frames:
        drop_label.place(
            x = grid_x * map_width,
            y = grid_y * map_height,
        )
        

    # 그렇지 않다면
    # >> 해당 레이블은 원 위치로 복귀 시킨다