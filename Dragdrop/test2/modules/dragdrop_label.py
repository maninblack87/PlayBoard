# modules/dragdrop_label.py
import tkinter as tk

class DragDropLabel(tk.Label):

    def __init__(self, master, drop_callback=None, **kwargs):
        super().__init__(master, **kwargs)
        self.drag_data = {"x": 0, "y": 0}
        self.drop_callback = drop_callback

    def on_start_drag(self, event):
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def on_drag_motion(self, event):
        new_winfo_x = self.winfo_x + (self.drag_data["x"] - event.x)
        new_winfo_y = self.winfo_y + (self.drag_data["y"] - event.y)
        self.place(
            x = new_winfo_x,
            y = new_winfo_y,
        )

    def on_drop(self, event):
        if self.drop_callback:
            self.drop_callback(self)

    def handle_drop(self, master, drop_label:tk.Label, map_frames:dict, map_width, map_height):

        # 드롭된 레이블(이하 레이블)의 그리드 상의 위치 값을 산출한다
        # 1. 메인 창 내에서 마우스 커서의 위치
        mouse_x_in_master = drop_label.winfo_pointerx() - master.winfo_x()
        mouse_y_in_master = drop_label.winfo_pointery() - master.winfo_y()
        
        # 2. 그리드 상의 위치
        grid_x = mouse_x_in_master // map_width
        grid_y = mouse_y_in_master // map_height
        
        # 만약 대상 프레임(들) 영역 내에 마우스 커서를 위치 시키면
        # >> 해당 레이블의 위치를 그리드 상으로 이동시킨다
        if (grid_x, grid_y) in map_frames:
            drop_label.place(
                x = grid_x * map_width,
                y = grid_y * map_height,
            )
            drop_label.origin_x = drop_label.grid_x * map_width
            drop_label.origin_y = drop_label.grid_y * map_height
            
        # 그렇지 않다면
        # >> 해당 레이블은 원 위치로 복귀 시킨다
        else:
            drop_label.place(
                x = drop_label.origin_x,
                y = drop_label.origin_y,
            )