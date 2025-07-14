# cards/card.py
import tkinter as tk

class Card:
    """
    슈퍼클래스
    """

    def __init__(self, name:str, color:str="colorless", type:str=None, cost:int=None, dur:int=None, pow:int=None, evergreen=None, effect:str=None):
        self.name = name
        self.color = color
        self.type = type
        self.cost = cost
        self.dur = dur
        self.pow = pow
        self.evergreen = evergreen          # 추후 해당객체 추가예정
        self.effect = effect

    def place_card(self, root, grid_w, grid_h, x:int=None, y:int=None, w:int=None, h:int=None):
        """
        root : 배치될 객체의 (기준)위치. 생성된 객체(Card)가 여러군데 원하는 위치에 배치할 수 있게됨
        grid_w, grid_h : '그리드'의 크기
        x, y : (그리드 기준) 객체를 배치할 위치좌표
        w, h : '객체'의 크기
        """

        card = tk.Label(
            root,
            text = f"{self.text}\n{self.color},\n{self.type}\n",
            borderwidth=1,
            relief="solid"
        )
        
        card.place(
            x = x * grid_w,
            y = y * grid_h,
            width = w,
            height = h
        )
    