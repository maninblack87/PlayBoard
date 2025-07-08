import tkinter as tk
import map

# 초기 설정
cols, rows = 4, 10
grid_w, grid_h = 100, 60

# 메인창
root = tk.Tk()
root.geometry(f"{cols*grid_w}x{rows*grid_h}")
root.title("테스트-mtg")
root.resizable(False, False)
root.option_add("Font", "Gothic 12")

# 매핑
map.Map(root, "frame", 10, 4, 100, 100)

# GUI 실행
root.mainloop()