def on_drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
    widget.tkraise()

def on_drag_motion(event):
    widget = event.widget
    widget.place(
        x = widget.winfo_x() - widget.startX + event.x,
        y = widget.winfo_y() - widget.startY + event.y
    )

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
            break