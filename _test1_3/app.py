import tkinter as tk
import dragdrop
import toggle_color

root = tk.Tk()
root.geometry("800x600")
root.resizable(False, False)
root.option_add("Font", "Gothic 12")

cols, rows = 8, 6
grid_w, grid_h = 100, 100
label_w, label_h = 90, 90

terrains = []
for y in range(rows):
    row = []
    for x in range(cols):

        label = tk.Label(
            root,
            text=f"{(y*cols)+x+1}",
            bg="SystemButtonFace",
            borderwidth=1,
            relief="solid",
        )

        label.place(x=x*grid_w, y=y*grid_h, width=label_w-((grid_w-label_w)/2), height=label_h-((grid_h-label_h)/2))

        label.bind("<Double-Button-1>", toggle_color.toggle_color)
        label.bind("<Button-1>", dragdrop.on_drag_start)
        label.bind("<B1-Motion>", dragdrop.on_drag_motion)
        label.bind(
            "<ButtonRelease-1>",
            lambda e, all_labels=None: dragdrop.on_drag_release(e, [label for row in terrains for label in row])
        )

        row.append(label)
    terrains.append(row)

root.mainloop()