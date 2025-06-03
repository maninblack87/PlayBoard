import tkinter as tk
from tkinter import messagebox

# 메인 창 생성
root = tk.Tk()
root.title("Starcraft")
root.geometry("800x600")
root.resizable(False, False)
root.option_add("Font", "Gothic 12")

# 그리드 레이아웃으로 배치
# 1) 맵 x, y축 변수 세팅(변수)
map_x = 8
map_y = 6
# 2) 맵 그리드 레이아웃 세팅
for i in range(map_x):
    root.columnconfigure(i, weight=1)
for i in range(map_y):
    root.rowconfigure(i, weight=1)

# 맵 지형배치
terrains = []
for y in range(map_y):
    row = []
    for x in range(map_x):
        label = tk.Label(root, text=f"{x},{y}", borderwidth=1, relief="solid", width=10, height=4, bg="lightgray")
        label.grid(row=y, column=x, sticky="nsew")
        row.append(label)
    terrains.append(row)
messagebox.showinfo("테스트", terrains)

# (테스트) 맵 일부 속성 설정
terrains[1][1].config(bg="green")

# 
root.mainloop()