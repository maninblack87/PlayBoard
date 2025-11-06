# handle_drop.py
import tkinter as tk
from dragdrop_label import DragDropLabel
from config import ROOT_HEIGHT, ROOT_WIDTH, MAP_HEIGHT, MAP_WIDTH, MAP_X, MAP_Y

def handle_drop(root:tk.Widget, drop_label:DragDropLabel|tk.Label, drop_frames:dict):

    # 현재 창(일반적으로 root) 기준으로 마우스 현재 위치 산출
    x_root = drop_label.winfo_pointerx() - root.winfo_rootx()
    y_root = drop_label.winfo_pointery() - root.winfo_rooty()

    # 그리드 인덱스 산출
    grid_x = x_root // MAP_WIDTH
    grid_y = y_root // MAP_HEIGHT

