import tkinter as tk
from dbconnect import connect_to_mysql
from query.query_editor import create_unit_table

# 최초 실행시
create_unit_table()

# 데이터베이스 연결
dbconn = connect_to_mysql()

# 메인 창
root = tk.Tk()
root.title("Test2")
root.geometry("300x300")
root.resizable(False, False)
root.option_add("Font", "Gothic 12")

# 변수
map_x = 3
map_y = 3
label_size = 100
slots = {}

# 슬롯 배치
for y in range(map_y):

    for x in range(map_x):

        # 그리드마다 슬롯 설정
        if x == 0 and y == 0:
            label = tk.Label(
                root,
                text = "플레이어1 빈 슬롯",
                bg="lightgray",
                borderwidth=1,
                relief="solid",
            )
        elif x == 2 and y == 0:
            label = tk.Label(
                root,
                text = "플레이어2 빈 슬롯",
                bg = "lightgray",
                borderwidth=1,
                relief="solid",
            )
        elif y == 2:
            label = tk.Label(
                root,
                text = f"유닛 슬롯{x+1}",
                bg = "lightgray",
                borderwidth=1,
                relief="ridge",
            )
        else:
            label = tk.Label(
                root,
                bg = "lightgray",
                borderwidth=0,
                relief="solid",
            )

        # 모든 슬롯 배치
        label.place(
            x = x * label_size,
            y = y * label_size,
            width = label_size,
            height = label_size,
        )
        slots[(x, y)] = label

# 메인 창으로 GUI 실행
root.mainloop()