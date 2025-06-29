#factory.py
import tkinter as tk

class Factory:
    """
    유닛을 생산하는 팩토리

    0. 생성자 : set_factory()를 즉시 실행
    1. set_factory: 팩토리 위젯을 생성하고 배치
    2. on_click: 팩토리 위젯을 클릭하면 add_unit()을 실행
    3. add_unit: 유닛을 생성하고 배치

    root : 부모 위젯
    label_w, label_h : 레이블 크기
    x, y : 레이블 위치(실제)
    text : 표시될 이름
    """

    # 생성자, set_factory()를 즉시 실행
    def __init__(self, root, pos_x, pos_y, label_w, label_h, text="팩토리"):
        self.root = root
        self.label_w = label_w
        self.label_h = label_h
        self.x = pos_x * self.label_w
        self.y = pos_y * self.label_h
        self.text = text

        # 팩토리 생성(및 배치) 메소드 호출
        self.set_factory()


    # 팩토리 위젯을 생성하고 배치
    def set_factory(self):

        # 팩토리 생성
        self.label = tk.Label(
            self.root, 
            text=self.text,
            relief="groove"
        )

        # 팩토리 배치
        self.label.place(x=self.x, y=self.y, width=self.label_w, height=self.label_h)

        # 클릭 이벤트 바인딩
        self.label.bind("<Button-1>", self.on_click)

    
    # (팩토리 위젯을) 클릭하면 해당 팩토리를 활성화 시키는 위젯
    def on_click(self, event): 
        
        return 0