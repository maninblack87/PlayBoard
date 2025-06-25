# tiling.py
import tkinter as tk

class Tiling:
    
    def __init__(self, root, map_x, map_y, tile_w, tile_h):
        """
        1) root : 맵이 만들어질 부모 창
        2) map_x, map_y : 맵 사이즈(단위: 타일개수)
        3) tile_w, tile_h : 타일 사이즈(w: 너비, h: 높이)
        4) tiles : 맵내 타일들의 딕셔너리

        맵 전체에 기본 타일을 배치한다
        """
        self.root = root
        self.map_x = map_x
        self.map_y = map_y
        self.tile_w = tile_w
        self.tile_h = tile_h
        self.tiles = {}

        # 맵 전체에 기본 타일을 배치한다
        self.base_tiling()

    def base_tiling(self) -> None:
        """
        그리드 전체에(xs, ys) 기본 타일(레이블)을 배치한다
        """
        for y in range(self.map_y):
            for x in range(self.map_x):
                label = tk.Label(
                    self.root,
                    text="",
                    bg="lightgray",
                    borderwidth=1,
                    relief="solid"
                )

                label.place(
                    x = x * self.tile_w,
                    y = y * self.tile_h,
                    width = self.tile_w,
                    height = self.tile_h
                )

                self.tiles[(x, y)] = label
    
    def update_tile(self, x: int, y: int, text: str = None, bg: str = None) -> None:
        """
        특정 그리드에(x, y) 타일(레이블)의 속성을 수정한다
        1) 텍스트
        2) 배경색상
        """
        # 지정된 타일
        tile = self.tiles.get((x, y))

        # 타일 속성을 수정한다
        if tile:
            if text is not None:
                tile.config(text=text)
            if bg is not None:
                tile.config(bg=bg)
        else:
            print("update_tile 오류 : 타일을 찾을 수 없습니다.")