#factory.py
import tkinter as tk

class Factory:
    """
    유닛을 생산하는 팩토리

    0. 생성자       : set_factory()를 즉시 실행
    1. set_factory : 팩토리 위젯을 생성하고 배치
    2. on_click    : 팩토리 위젯을 클릭하면 활성화 실행,
    3. add_unit    : 유닛을 생성하고 배치

    root           : 부모 위젯
    grid_w, grid_h : 부모 위젯의 그리드 크기
    fac_w, fac_h   : 레이블 크기
    x, y           : 레이블 위치(실제)
    fac_name       : 표시될 이름
    """

    # 생성자, set_factory()를 즉시 실행
    def __init__(self, root, grid_w, grid_h, pos_x, pos_y, fac_w, fac_h, fac_name="팩토리"):
        self.root = root        # 부모 위젯
        self.grid_w = grid_w    # (부모 위젯의) 그리드 너비
        self.grid_h = grid_h    # (부모 위젯의) 그리드 높이
        self.fac_w = fac_w      # 팩토리의 너비
        self.fac_h = fac_h      # 팩토리의 높이
        self.x = pos_x * self.grid_w        # 팩토리가 위치할 그리드의 위치 x축
        self.y = pos_y * self.grid_h        # 팩토리가 위치할 그리드의 위치 y축
        self.fac_name = fac_name        # 팩토리 이름

        # 팩토리 생성
        self.factory = tk.Label(
            self.root,
            text = fac_name,
            relief = "solid"
        )

        # 팩토리 활성화 여부
        self.is_active : bool = False

        # 팩토리 생성(및 배치) 메소드 호출
        self.set_factory()


    # 팩토리 위젯을 생성하고 배치
    def set_factory(self):

        # 팩토리 배치
        self.factory.place(
            x=self.x + (self.grid_w - self.fac_w)/2,
            y=self.y + (self.grid_h - self.fac_h)/2, 
            width=self.fac_w, 
            height=self.fac_h
        )

        # 클릭 이벤트 바인딩
        self.factory.bind("<Button-1>", self.on_click)

    
    # (팩토리 위젯을) 클릭하면 해당 팩토리를 활성화 시키는 위젯
    def on_click(self, event): 
        
        if self.is_active == True:

            # 비활성화 표시
            self.factory.config(
                highlightbackground="black",
                highlightthickness=0
            )

            # 팩토리의 활성화 여부 False로 갱신
            self.is_active = False

        else:

            # 활성화 표시
            self.factory.config(
                highlightbackground="green",
                highlightthickness=3
            )

            # 팩토리의 활성화 여부 True로 갱신
            self.is_active = True