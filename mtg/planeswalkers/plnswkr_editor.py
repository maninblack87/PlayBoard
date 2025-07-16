# planeswalkers/plnswkr_editor.py

import tkinter as tk
from .planeswalker import Planeswalker

root = tk.Tk()
root.title("테스트(생성)")
root.geometry("600x300+0+0")
root.option_add("Font", "Gothic 12")

# 좌측 프레임
lframe = tk.Frame(root, borderwidth=1, relief="solid")
lframe.place( x = 0, y = 0, width = 300, height = 300)
# 우측 프레임
rframe = tk.Frame(root, borderwidth=1, relief="solid")
rframe.place(x = 300, y = 0, width = 300, height = 300)

# 입력1 셋을 위한 별도의 프레임 생성
frame1 = tk.Frame(lframe)
frame1.pack(side="top", anchor="nw")
name_lbl = tk.Label(frame1, text="입력1", width=10, height=1)
name_lbl.pack(side="left")
name_ipt = tk.Entry(frame1, width=25)
name_ipt.pack(side="left")

# 입력2 셋을 위한 별도의 프레임 생성
frame2 = tk.Frame(lframe)
frame2.pack(side="top", anchor="nw")
hitpoint_lbl = tk.Label(frame2, text="입력2", width=10, height=1)
hitpoint_lbl.pack(side="left")
hitpoint_ipt = tk.Entry(frame2, width=10)
hitpoint_ipt.pack(side="left")

# 입력a 셋을 위한 별도의 프레임 생성
frame3 = tk.Frame(lframe)
frame3.pack(side="top", anchor="nw")
bonus_lbl = tk.Label(frame3, text="입력3 셋", width=50, height=1, bg="lightgray")
bonus_lbl.pack(side="top")

# 입력3 셋 _ 1
frame3_1 = tk.Frame(lframe)
frame3_1.pack(side="top", anchor="nw")
# white
white_lbl = tk.Label(frame3_1, text="화이트", width=5, height=1)
white_lbl.pack(side="left")
white_ipt = tk.Entry(frame3_1, width=5)
white_ipt.pack(side="left", padx=5)
# red
red_lbl = tk.Label(frame3_1, text="레드", width=5, height=1)
red_lbl.pack(side="left")
red_ipt = tk.Entry(frame3_1, width=5)
red_ipt.pack(side="left", padx=5)
# blue
blue_lbl = tk.Label(frame3_1, text="블루", width=5, height=1)
blue_lbl.pack(side="left")
blue_ipt = tk.Entry(frame3_1, width=5)
blue_ipt.pack(side="left", padx=5)

# 입력3 셋 _ 2
frame3_2 = tk.Frame(lframe)
frame3_2.pack(side="top", anchor="nw")
# green
green_lbl = tk.Label(frame3_2, text="그린", width=5, height=1)
green_lbl.pack(side="left")
green_ipt = tk.Entry(frame3_2, width=5)
green_ipt.pack(side="left", padx=5)
# black
black_lbl = tk.Label(frame3_2, text="블랙", width=5, height=1)
black_lbl.pack(side="left")
black_ipt = tk.Entry(frame3_2, width=5)
black_ipt.pack(side="left", padx=5)

root.mainloop()