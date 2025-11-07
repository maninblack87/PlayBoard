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