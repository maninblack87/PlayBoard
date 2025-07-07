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

# 드래그 드롭 놓을때 작동시킬 예정임
def on_drag_release(event, all_labels):
    """
    all_labels : 부모 위젯 내 모든 레이블 >> root가 부모 위젯이면 그 안에 배치된 모든 레이블을 가리킨다
    """

    # (드래그 드롭 놓을때) 위젯
    dragged = event.widget

    # (드래그 드롭 놓을때) 마우스 포인터의 '화면상' 위치좌표
    x_root = event.x_root
    y_root = event.y_root

    # 드래그 드롭이 어느 레이블 위에서 드롭되었는지 검사해서
    # 드래그 드롭한 레이블의 속성으로 변환시킨다
    for target in all_labels:

        # 검사대상(target)이 내가 드래그한 자기자신(dragged)이면 
        # 이번 조건(의 반복문)은 무시하고 다음 조건(의 반복문)으로 넘어가라
        if target == dragged:
            continue

        # 위젯의 위치와 크기 정보
        tx = target.winfo_rootx()
        ty = target.winfo_rooty()
        tw = target.winfo_width()
        th = target.winfo_height()

        # 마우스포인터가 검사대상이 되는 위젯안에 있으면
        # 해당 위젯의 속성을 드래그한 레이블(dragged)의 속성으로 갖다붙인다
        if (tx <= x_root <= tx + tw) and (ty <= y_root <= ty + th):

            target.config(
                text = dragged.cget("text"),
                bg = dragged.cget("bg")
            )