import tkinter as tk
import dragdrop
import toggle_color

root = tk.Tk()
root.geometry("800x600")
root.option_add("Font", "Gothic 12")

cols, rows = 8, 6
label_size = 90  # 너비와 높이 설정

terrains = []
for y in range(rows):
    row = []
    for x in range(cols):
        label = tk.Label(
            root,
            text=f"{x},{y}",
            bg="SystemButtonFace",
            borderwidth=1,
            relief="solid",
            width=10,
            height=4
        )
        label.place(x=x * label_size, y=y * label_size)

        label.bind("<Double-Button-1>", toggle_color.toggle_color)
        label.bind("<Button-1>", dragdrop.on_drag_start)
        label.bind("<B1-Motion>", dragdrop.on_drag_motion)
        label.bind(
            "<ButtonRelease-1>",
            lambda e, all_labels=None: dragdrop.on_drag_release(e, [lbl for row in terrains for lbl in row])
        )

        row.append(label)
    terrains.append(row)

root.mainloop()