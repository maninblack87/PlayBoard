# app.py
import tkinter as tk

# 맵 설정
cnt_x = 9
cnt_y = 9
map_w = 80
map_h = 80

# 메인창 생성
root = tk.Tk()
root.title("Blue Marble")
root.geometry(f"{cnt_x*map_w}x{cnt_y*map_h}+0+0")
root.resizable(False, False)
root.option_add("Font", "Gothic 12")

# 매핑 - 프레임
corner_frame = []   # 모서리 프레임을 저장할 리스트
top_frame = []
bottom_frame = []
lside_frame = []
rside_frame = []
for y in range(cnt_y):
    for x in range(cnt_x):

        # 코너 프레임
        if x in [0, 8] and y in [0, 8]:
            corner = tk.Frame(root, bg="#fff", width=map_w, height=map_h, border=1, relief="solid")
            corner.place(x=x*map_w, y=y*map_h)
            corner_frame.append(corner)

        # 상단 프레임
        if x in range(1, 8) and y == 0:
            top = tk.Frame(root, bg="#ffa", width=map_w, height=map_h, border=1, relief="solid")
            top.place(x=x*map_w, y=y*map_h)
            top_frame.append(top)

        # 하단 프레임
        if x in range(1, 8) and y == 8:
            bottom = tk.Frame(root, bg="#cfc", width=map_w, height=map_h, border=1, relief="solid")
            bottom.place(x=x*map_w, y=y*map_h)
            bottom_frame.append(bottom)

        # 좌측 프레임
        if x == 0 and y in range(1, 8):
            lside = tk.Frame(root, bg="#aff", width=map_w, height=map_h, border=1, relief="solid")
            lside.place(x=x*map_w, y=y*map_h)
            lside_frame.append(lside)

        # 우측 프레임
        if x == 8 and y in range(1, 8):
            rside = tk.Frame(root, bg="#fcc", width=map_w, height=map_h, border=1, relief="solid")
            rside.place(x=x*map_w, y=y*map_h)
            rside_frame.append(rside)

# 매핑 - 레이블
corners = []
corner_map_name = ["올림픽", "세계여행", "무인도", "시작"]
for i in range(len(corner_frame)):
    corner = tk.Label(corner_frame[i], text=corner_map_name[i], bg="#eee")
    corner.place(x=0, y=0, width=map_w, height=map_h)

# 메인창 GUI 활성화
root.mainloop()