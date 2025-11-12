# handle_drop.py
import tkinter as tk
from dragdrop_label import DragDropLabel

def handle_drop(drop_label, *, root, x_cnt, y_cnt, grid_w, grid_h):

    # 현재 창(일반적으로 root) 기준으로 마우스 현재 위치 산출
    mouse_x_in_root = drop_label.winfo_pointerx() - root.winfo_rootx()
    mouse_y_in_root = drop_label.winfo_pointery() - root.winfo_rooty()

    # 그리드 인덱스 산출
    drop_label.grid_x = mouse_x_in_root // grid_w
    drop_label.grid_y = mouse_y_in_root // grid_h

    # (정상적인 상황) 지정된 프레임(들) 안에서 마우스 커서의 위치가 잡힐 때
    is_allowed = 0 <= mouse_x_in_root < x_cnt * grid_w and 0<= mouse_y_in_root < y_cnt * grid_h
    if is_allowed:
        # (드롭된 위치의) 그리드 인덱스 산출
        drop_label.place(
            x = drop_label.grid_x * grid_w,
            y = drop_label.grid_y * grid_h,
        )
        # 새로 이동된 레이블의 위치 정보를 정의한다
        drop_label.origin_placed_x = drop_label.grid_x * grid_w
        drop_label.origin_placed_y = drop_label.grid_y * grid_h

    # (비정상적인 상황) 지정된 프레임(들) 안에서 마우스 커서의 위치가 잡히지 않을 때
    else:
        # 레이블을 원 위치로 되돌린다
        drop_label.place(
            x = drop_label.origin_placed_x,
            y = drop_label.origin_placed_y,
        )