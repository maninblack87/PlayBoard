import tkinter as tk
import dragdrop
import toggle_color

# 메인창 생성
root = tk.Tk()
root.geometry("800x600")
root.option_add("Font", "Gothic 12")

# 변수값 
# 1) 그리드 레이아웃상에서 행/열의 개수 설정
cols, rows = 8, 6
# 2) 레이블 크기 설정
label_size = 90  # 너비와 높이 설정

# 지형 배열
terrains = []
# 행 반복
for y in range(rows):
    row = []
# 열 반복
    for x in range(cols):

        # 각 그리드마다 레이블 생성&배치
        label = tk.Label(
            root,
            text=f"{x+(y*cols)+1}",
            bg="SystemButtonFace",
            borderwidth=1, 
            relief="solid",
            width=10, 
            height=4
        )
        label.place(x=x * label_size, y=y * label_size)

        # 해당 레이블 이벤트
        # 1) 색상 변환
        label.bind("<Double-Button-1>", toggle_color.toggle_color)
        # 2) 드래그 드롭
        label.bind("<Button-1>", dragdrop.on_drag_start)
        label.bind("<B1-Motion>", dragdrop.on_drag_motion)
        label.bind(
            "<ButtonRelease-1>",
            lambda e, all_labels=None: dragdrop.on_drag_release(e, [label for row in terrains for label in row])
            # !! 참고 !!
            # [label for row in terrains for label in row]은 terrains 모든 레이블을 가리킴
            # 이것은 2차 반복문이니까
        )
        # (반복문:x축) row배열에 레이블 추가
        row.append(label)
    # (반복문:y축) 지형 배열에 row추가
    terrains.append(row)

# 
root.mainloop()