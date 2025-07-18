# map.py

import tkinter as tk

class Map:

    def __init__(self, root:tk.Label|tk.Frame=None, type:str="frame", start_col:int=None, start_row:int=None, cols:int=None, rows:int=None, grid_w:int=None, grid_h:int=None, width:int|None=None, height:int|None=None):
        self.root = root
        self.start_col = start_col
        self.start_row = start_row
        self.cols = cols
        self.rows = rows
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
        for y in range(self.start_row, self.start_row + self.rows):
            row = []
            for x in range(self.start_col, self.start_col + self.cols):
                
                frame = tk.Frame(
                    self.root,
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
        for y in range(self.start_row, self.start_row + self.rows):
            row = []
            for x in range(self.start_col, self.start_col + self.cols):
                
                label = tk.Label(
                    self.root,
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

    # 배경색 변경
    def modify_bg(self, start_col:int=None, start_row:int=None, cols:int=None, rows:int=None, bg:str=None):
        for y in range(start_row, start_row + rows):
            for x in range(start_col, start_col + cols):
                label = self.map[y][x]
                if bg:
                    label.config(bg=bg)

    # 텍스트 변경
    def modify_text(self, start_col:int=None, start_row:int=None, cols:int=None, rows:int=None, text:str=None):
        for y in range(start_row, start_row + rows):
            for x in range(start_col, start_col + cols):
                label = self.map[y][x]
                if text:
                    label.config(text=text)

    # TEST - 맵 리스트 출력
    def print_map(self):
        print(self.map)