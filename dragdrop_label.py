# dragdrop_label.py
import tkinter as tk

# tk.Label으로부터 상속받는 클래스
# 즉, 부모 클래스(super)는 tk.Label을 가리킴
class DragDropLabel(tk.Label):
    
    def __init__(self, master, drop_callback=None, **kwargs):
        """
        1) master : 해당 위젯(레이블)을 포함하는 부모 위젯을 의미.
        2) drop_callback : "드래그가 끝나고 놓였을때" 호출할 콜백 함수를 받을 인자.
        3) **kwargs : 추가적인 키워드 인자. (예: text=, bg=, font=)
        """
        super().__init__(master, **kwargs)      # 부모 클래스(tk.Label)로부터 레이블의 속성을 상속 받음
        self.drag_data = {"x": 0, "y": 0}
        self.drop_callback = drop_callback

        self.bind("<Button-1>", self.on_start_drag)
        self.bind("<B1-Motion>", self.on_drag_motion)
        self.bind("<ButtonRelease-1>", self.on_drop)

    def on_start_drag(self, event):
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y
        self.lift()

    def on_drag_motion(self, event):
        new_x = self.winfo_x() + (event.x - self.drag_data["x"])
        new_y = self.winfo_y() + (event.y - self.drag_data["y"])
        self.place(x=new_x, y=new_y)

    def on_drop(self, event):
        if self.drop_callback:
            self.drop_callback(self)
