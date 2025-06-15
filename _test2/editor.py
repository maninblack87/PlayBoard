import tkinter as tk
from dbconnect import connect_to_mysql
import modules.add_image as add_image

# 데이터베이스 연결
dbconn = connect_to_mysql()

# 메인창
root = tk.Tk()
root.title("에디터")
root.geometry("400x300")
root.resizable(False, False)
root.option_add("Font", "Gothic 12")

# 1. 프레임1 : 이름
frame1 = tk.Frame(root, borderwidth=1, relief="solid", padx=10, pady=10)  # 내부 패딩 추가
frame1.pack(fill='x', padx=10, pady=5)  # 외부 패딩 추가, 위쪽 10, 아래쪽 5
# 1-1. 이름
lbl_name = tk.Label(frame1, text="이름")
lbl_name.grid(row=0, padx=10, pady=5)  # 오른쪽에 공간
ipt_name = tk.Entry(frame1)
ipt_name.grid(row=0, column=1, padx=10, pady=5)  # 입력칸은 가로로 확장

# 2. 프레임2 : 이미지
frame2 = tk.Frame(root, borderwidth=1, relief="solid", padx=10, pady=10)
frame2.pack(fill='x', padx=10, pady=5)
# 2-1. 이미지
lbl_img = tk.Label(frame2, text="이미지")
lbl_img.grid(row=0, column=0, padx=10, pady=5)
btn_choose_img = tk.Button(frame2, text="이미지 등록", command=lambda: add_image.choose_image(loaded_img))
btn_choose_img.grid(row=0, column=1, padx=10, pady=5)
loaded_img = tk.Label(frame2)
loaded_img.grid(row=0, column=2, padx=10, pady=5)

# 3. 프레임 : 유닛의 공격력, 내구도
frame3 = tk.Frame(root, borderwidth=1, relief="solid")
frame3.pack(fill='x', padx=10, pady=10)
# 3-1. 공격력
lbl_atk = tk.Label(frame3, text="공격력")
lbl_atk.grid(row=0, column=0, padx=10, pady=5)
ipt_atk = tk.Entry(frame3)
ipt_atk.grid(row=0, column=1, padx=10, pady=5)
# 3-2. 내구도
lbl_dur = tk.Label(frame3, text="내구도")
lbl_dur.grid(row=1, column=0, padx=10, pady=5)
ipt_dur = tk.Entry(frame3)
ipt_dur.grid(row=1, column=1, padx=10, pady=5)

# 등록

# 취소

# 메인창으로 GUI실행
root.mainloop()
