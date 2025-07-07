import tkinter as tk
import dragdrop
import toggle_color

root = tk.Tk()
root.geometry("800x600")
root.option_add("Font", "Gothic 12")

cols, rows = 8, 6
label_size = 90

terrains = []
for y in range(rows):
    row = []
    for x in range(cols):
        
        # 각 좌표마다 레이블을 생성 & 배치하고, 이벤트를 연결시킨다.
        # 레이블 생성
        label = tk.Label(
            root,
            text=f"{(y*cols)+x+1}",
            bg="white",
            borderwidth=1,
            relief="solid",
            width=10,
            height=4
        )

        # 레이블 배치
        label.place(x = x*label_size, y = y*label_size)

        # 레이블 이벤트
        label.bind("<Double-Button-1>", toggle_color.toggle_color)
        label.bind("<Button-1>", dragdrop.on_drag_start)
        label.bind("<B1-Motion>", dragdrop.on_drag_motion)
        label.bind(
            "<ButtonRelease-1>",
            lambda e, all_labels=None: dragdrop.on_drag_release(e, [label for row in terrains for label in row])
        )

        # 행에 각 레이블 추가
        row.append(label)
    terrains.append(row)

root.mainloop()