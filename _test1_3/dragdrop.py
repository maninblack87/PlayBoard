def on_drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
    widget.tkraise()

def on_drag_motion(event):
    widget = event.widget
    widget.place(
        # widget.winfo_x() : 위젯의 '이벤트 발생 전' 위치
        # widget.startX    : 마우스포인터의 '이벤트 발생 전' 위치
        # event.x          : 마우스포인터의 '이벤트 발생 후' 위치
        x = widget.winfo_x() + event.x - widget.startX,
        y = widget.winfo_y() + event.y - widget.startY
    )

def on_drag_release(event, all_labels):
    dragged = event.widget  # '이벤트 발생 후' 위젯
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