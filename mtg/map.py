import tkinter as tk

class Map:

    def __init__(self, parent_widget:tk.Label|tk.Frame=None, type:str="frame", rows:int=None, cols:int=None, grid_w:int=None, grid_h:int=None, width:int|None=None, height:int|None=None):
        self.parent_widget = parent_widget
        self.rows = rows
        self.cols = cols
        self.grid_w = grid_w
        self.grid_h = grid_h
        if not width and not height:
            self.width = grid_w
            self.height = grid_h
        if type == "frame":
            self.set_frame()
        elif type == "label":
            self.set_label()

    def set_frame(self):
        map = []
        for y in range(self.rows):
            row = []
            for x in range(self.cols):
                
                frame = tk.Frame(
                    self.parent_widget,
                    borderwidth=1,
                    relief="solid"
                )

                frame.place(
                    x = x * self.grid_w,
                    y = y * self.grid_h,
                    width = self.width,
                    height = self.height
                )

                row.append(frame)

            map.append(row)

    def set_label(self):
        map = []
        for y in range(self.rows):
            row = []
            for x in range(self.cols):
                
                label = tk.Label(
                    self.parent_widget
                )

                label.place(
                    x = x * self.grid_w,
                    y = y * self.grid_h,
                    width = self.width,
                    height = self.height
                )

                row.append(label)

            map.append(row)