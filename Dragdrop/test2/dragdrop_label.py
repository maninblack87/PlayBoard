# dragdrop_label.py
import tkinter as tk

class DragDropLabel(tk.Label):

    def __init__(self, master, drop_callback=None, **kwargs):
        super().__init__(master, **kwargs)
        self.drag_data = {"x": 0, "y": 0}
        self.drop_callback = drop_callback

        # bind functions
        self.bind("<Button-1>", self.on_start_drag)
        self.bind("<B1-Motion>", self.on_drag_motion)
        self.bind("<ButtonRelease-1>", self.on_drop)

    def on_start_drag(self, event):
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def on_drag_motion(self, event):
        new_winfo_x = self.winfo_x() + (event.x - self.drag_data["x"])
        new_winfo_y = self.winfo_y() + (event.y - self.drag_data["y"])
        self.place(x = new_winfo_x, y = new_winfo_y)

    def on_drop(self, event):
        if self.drop_callback:
            self.drop_callback(self)