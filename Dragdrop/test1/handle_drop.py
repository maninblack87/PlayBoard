# handle_drop.py
import tkinter as tk
from dragdrop_label import DragDropLabel

def handle_drop(root:tk.Widget, drop_frames:dict, drop_label:DragDropLabel|tk.Label, map_width:int, map_height:int):
    """
    레이블(드래그드롭 레이블) 드롭 함수
    mouse_x_in_root: 창(root) 위젯을 기준으로 한 마우스 커서의 X 좌표 위치
    """

    # 현재 창(일반적으로 root) 기준으로 마우스 현재 위치 산출
    mouse_x_in_root = drop_label.winfo_pointerx() - root.winfo_rootx()
    mouse_y_in_root = drop_label.winfo_pointery() - root.winfo_rooty()

    # 그리드 인덱스 산출
    drop_label.grid_x = mouse_x_in_root // map_width
    drop_label.grid_y = mouse_y_in_root // map_height

    # (정상적인 상황) 지정된 프레임(들) 안에서 마우스 커서의 위치가 잡힐 때
    if (drop_label.grid_x, drop_label.grid_y) in drop_frames:

        # (드롭된 위치의) 그리드 인덱스 산출
        drop_label.place(
            x = drop_label.grid_x * map_width,
            y = drop_label.grid_y * map_height,
        )

        # 새로 이동된 레이블의 위치 정보를 정의한다
        drop_label.origin_placed_x = drop_label.grid_x * map_width
        drop_label.origin_placed_y = drop_label.grid_y * map_height

    # (비정상적인 상황) 지정된 프레임(들) 안에서 마우스 커서의 위치가 잡히지 않을 때
    else:

        # 레이블을 원 위치로 되돌린다
        drop_label.place(
            x = drop_label.grid_x * map_width,
            y = drop_label.grid_y * map_height,
        )