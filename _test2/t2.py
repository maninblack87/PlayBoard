import tkinter as tk

# 1. 메인창 생성 및 설정
root = tk.Tk()
root.title("테스트2")
root.geometry("800x600")
root.resizable(False, False)
root.option_add("Font", "Gothic 10")

# 2. 그리드 레이아웃
cols, rows = 8, 6
label_size = 90

# 3. 레이블 생성(그리드 레이아웃을 바탕으로)
terrains = []
for row in range(rows):
    row_labels = []

    for col in range(cols):
        label = tk.Label(
            root, 
            text="레이블{}",
            bg="SystemButtonFace",
            borderwidth=1,
            relief="solid",
            width=10,
            height=4
            )
        label.place(x = col * label_size, y = row * label_size)
        row_labels.append(label)

        
        
    terrains.append(row_labels)


# 4. 이벤트 설정

# 4-1. 더블클릭 이벤트 -> 레이블 색상변경

# 4-2. 드래그드롭 이벤트 -> 레이블 속성 붙여넣기

# last. 메인창으로 GUI
root.mainloop()