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
def handle_drop(unit_label):

    # 메인창(root)의 좌측상단으로부터 마우스의 위치 산출
    # winfo_pointerx() : 마우스의 위치
    # winfo_rootx() : 창의 좌상단의 위치
    x_root = unit_label.winfo_pointerx() - root.winfo_rootx()
    y_root = unit_label.winfo_pointery() - root.winfo_rooty()

    # 그리드 인덱스 산출
    grid_x = x_root // label_size
    grid_y = y_root // label_size

    # 
    if (grid_x, grid_y) in slots:
        unit_label.place(
            x=grid_x * label_size,
            y=grid_y * label_size
        )
        unit_label.origin_x = grid_x * label_size
        unit_label.origin_y = grid_y * label_size
    else:
        unit_label.place(
            x=unit_label.origin_x,
            y=unit_label.origin_y
        )

# ✅ 슬롯 배치
for y in range(map_y):
    for x in range(map_x):
        if x in [0, 7] and y in [0, 1, 2]:
            label = tk.Label(
                root,
                text="고정 슬롯",
                bg="lightgray",
                borderwidth=1,
                relief="solid"
            )
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
        else:
            continue

        label.place(
            x=x * label_size,
            y=y * label_size,
            width=label_size,
            height=label_size
        )
        slots[(x, y)] = label

root.mainloop()