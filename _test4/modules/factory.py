#factory.py
import tkinter as tk

class Factory:
    """
    """

    def __init__(self, root, pos_x, pos_y, label_w, label_h, text="팩토리"):
        self.root = root
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.label_w = label_w
        self.label_h = label_h
        self.text = text

        # 실제 위치(픽셀) 정의
        self.x = pos_x * self.label_w
        self.y = pos_y * self.label_h

        self.set_factory()

    def set_factory(self):
        label = tk.Label(
            self.root, 
            text=self.text,
            relief="solid"
        )
        label.place(x=self.x, y=self.y, width=self.label_w, height=self.label_h)
