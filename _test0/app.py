import tkinter as tk
from dragdrop_label import DragDropLabel
from unit_factory import create_unit  # 🔽 유닛 생성 함수 import
from unit_events import spawn_unit  # 👈 새로운 파일에서 import

root = tk.Tk()
root.title("Starcraft")
root.geometry("800x700")
root.resizable(False, False)
root.option_add("Font", "Gothic 12")

map_x = 8
map_y = 7
label_size = 90
slots = {}

# 드롭 처리 함수
def handle_drop(unit_label:tk.Label):

    # x_root : 마우스의 현재 위치(상대좌표) 산출
    # winfo_pointerx() : 화면 기준 마우스 좌표 
    # winfo_rootx() : 창의 좌상단의 좌표
    x_root = unit_label.winfo_pointerx() - root.winfo_rootx()
    y_root = unit_label.winfo_pointery() - root.winfo_rooty()

    # (드롭된 위치의) 그리드 인덱스 산출
    grid_x = x_root // label_size
    grid_y = y_root // label_size

    # 드롭의 위치가 (모든 레이블이 들어있는) 슬롯 안에 있는지 확인
    # 슬롯안에 없으면 원위치로 돌아가게한다
    # >> grid_x : 그리드 상의 위치
    # >> origin_x : 드래그 전의 레이블의 위치(보통 유닛 레이블을 가리킴)
    if (grid_x, grid_y) in slots:

        # 레이블을 정확한 위치로 이동시키는 코드
        unit_label.place(
            x=grid_x * label_size,
            y=grid_y * label_size
        )

        # 유닛의 현재 위치를 origin 위치로 업데이트
        unit_label.origin_x = grid_x * label_size
        unit_label.origin_y = grid_y * label_size

    else:
        
        # 슬롯안에 없으면 원위치로 돌아가게한다
        unit_label.place(
            x=unit_label.origin_x,
            y=unit_label.origin_y
        )

# 슬롯 배치
for y in range(map_y):
    for x in range(map_x):

        # 상단 양쪽 사이드 레이블에 "고정슬롯" 생성
        if x in [0, 7] and y in [0, 1, 2]:
            label = tk.Label(
                root,
                text="고정 슬롯",
                bg="lightgray",
                borderwidth=1,
                relief="solid"
            )

        # 하단 3개 행의 모든 레이블에 "유닛을 생산하는(번호 포함됨) 레이블"을 생성
        elif y in [4, 5, 6]:
            label = tk.Label(
                root,
                text=f"유닛 {(y-4)*map_x+x+1}",
                bg="white",
                borderwidth=1,
                relief="ridge"
            )
            # 클릭 -> 유닛 생산
            label.bind("<Button-1>", lambda e, x=x, y=y: spawn_unit(e, root, x, y, label_size, handle_drop))

        # 나머지는 건너뛰기(레이블 배치도 건너뜀)
        else:
            continue

        # 레이블 배치
        label.place(
            x=x * label_size,
            y=y * label_size,
            width=label_size,
            height=label_size
        )
        slots[(x, y)] = label

root.mainloop()