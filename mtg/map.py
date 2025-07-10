import tkinter as tk

class Map:

    def __init__(self, parent_widget:tk.Label|tk.Frame=None, type:str="frame", rows:int=None, cols:int=None, grid_w:int=None, grid_h:int=None, width:int|None=None, height:int|None=None):
        self.parent_widget = parent_widget
        self.rows = rows
        self.cols = cols
        self.grid_w = grid_w
        self.grid_h = grid_h
        self.map = []
        if not width and not height:
            self.width = grid_w
            self.height = grid_h
        if type == "frame":
            self.set_frame()
        elif type == "label":
            self.set_label()

    # 면적만큼 프레임 생서
    def set_frame(self):
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

            self.map.append(row)

    # 면적만큼 레이블 생성
    def set_label(self):
        for y in range(self.rows):
            row = []
            for x in range(self.cols):
                
                label = tk.Label(
                    self.parent_widget,
                    borderwidth=1,
                    relief="solid",
                    text="레이블"
                )

                label.place(
                    x = x * self.grid_w,
                    y = y * self.grid_h,
                    width = self.width,
                    height = self.height
                )

                row.append(label)

            self.map.append(row)

    # 텍스트 생성
    def set_text(self, text:str = None):
        for row in self.map:
            for label in row:
                label.config(text=text) 
    
    # TEST - 맵 리스트 출력
    def print_map(self):
        print(self.map)