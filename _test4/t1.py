import tkinter as tk

# 드래그드롭 시작
def dragdrop_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
    widget.tkraise()            # z-index를 최고레벨
    # << 참고 >>
    # widget.startX : 드래그드롭 시작시 위젯의 '시작'위치

# 드래그 드롭 모션
def on_drag_motion(event):
    widget = event.widget
    # 위젯을 내려놓는다
    widget.place(
        x = widget.winfo_x() - widget.startX + event.x,
        y = widget.winfo_y() - widget.startY + event.y
    )
    # << 참고 >>
    # widget.winfo_x() : 위젯의 '현재'위치
    # widget.startX    : 위젯의 '현재 직전'위치

# 드래그 드롭 끝
def on_drag_release(event, all_labels):
    dragged = event.widget
    x_root = event.x_root       # x_root는 스크린(모니터) 기준의 마우스 커서 절대좌표
    y_root = event.y_root

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
                text = dragged.cget("text"),
                bg = dragged.cget("bg")
            )
            break

# 메인창 생성
root = tk.Tk()
root.title("t1 드래그드롭 테스트")
root.geometry("500x400")
root.resizable(False, False)

# 그리드 설정
map_x = 5
map_y = 4
label_size = 100
slots = {}

# 슬롯배치
for y in range(map_y):
    for x in range(map_x):
        label = tk.Label(
                root,
                text=f"슬롯{y * map_x + x + 1}",
                bg="lightgray",
                borderwidth=1,
                relief="solid"
        )
        # 클릭 -> 유닛 생산
        
        label.place(
            x=x * label_size,
            y=y * label_size,
            width=label_size,
            height=label_size
        )
        slots[(x, y)] = label


root.mainloop()