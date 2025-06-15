# 드래그 드롭 시작시 작동 함수
def on_drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
    widget.tkraise()

# 드래그 드롭롭
def on_drag_motion(event):
    widget = event.widget
    widget.place(
        x=widget.winfo_x() - widget.startX + event.x,
        y=widget.winfo_y() - widget.startY + event.y
    )
    # !! 참고 !!
    # widget.winfo_x() = 위젯의 <<현재>> 위치
    # widget.startX = 위젯내에서 마우스 포인터의 <<시작점>> 위치
    # event.x = 위젯내에서 마우스 포인터의 <<현재>> 위치

def on_drag_release(event, all_labels):
    dragged = event.widget
    x_root = event.x_root   # (참고) x_root는 스크린(모니터) 기준의 마우스 커서 절대좌표
    y_root = event.y_root   # (참고) y_root는 스크린(모니터) 기준의 마우스 커서 절대좌표

    for target in all_labels:

        # 체크할 label(target)과 드래그 대상인 label(dragged)이 동일하면 로직을 중단하고
        # 즉시 다음 label로 로직 수행
        if target == dragged:
            continue

        # 이벤트가 발생한 시점의 실제 위치와 크기
        tx = target.winfo_rootx()
        ty = target.winfo_rooty()
        tw = target.winfo_width()
        th = target.winfo_height()

        # 마우스 포인터가 다른 레이블의 영역 안에 있으면 겹침
        if (tx <= x_root <= tx + tw) and (ty <= y_root <= ty + th):
            
            # 속성 복사
            target.config(
                text=dragged.cget("text"),
                bg=dragged.cget("bg")
            )
            break