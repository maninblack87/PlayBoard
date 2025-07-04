# 드래그를 시작할때 작동시킬 예정임
def on_drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
    widget.tkraise()

# 드래그 중에 (계속적으로) 작동시킬 예정임
def on_drag_motion(event):
    widget = event.widget
    widget.place(
        x = widget.winfo_x() - widget.startX + event.x,
        y = widget.winfo_y() - widget.startY + event.y
    )

# 드래그 드롭 놓을때
def on_drag_release(event, all_labels):
    dragged = event.widget
    x_root = event.x_root
    y_root = event.y_root

    for target in all_labels:

        if target == dragged:
            continue

        tx = target.winfo_rootx()
        ty = target.winfo_rooty()
        tw = target.winfo_width()
        th = target.winfo_height()

        if (tx <= x_root <= tx + tw) and (ty <= y_root <= ty + th):

            target.config(
                text = dragged.cget("text"),
                bg = dragged.cget("bg")
            )