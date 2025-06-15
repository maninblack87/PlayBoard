# unit_factory.py
from dragdrop_label import DragDropLabel

def create_unit(root, x, y, label_size, drop_callback, text="유닛", color="skyblue"):
    unit = DragDropLabel(
        root,
        text=f"{text}",
        bg=color,
        relief="raised",
        borderwidth=2,
        drop_callback=drop_callback
    )
    px = x * label_size
    py = y * label_size
    unit.place(
        x=px,
        y=py,
        width=label_size,
        height=label_size
    )
    unit.origin_x = px
    unit.origin_y = py
    return unit
