# 클릭 시 색상 토글 함수
def toggle_color(event):
    widget = event.widget
    current_bg = widget.cget("bg")
    if current_bg == "SystemButtonFace":
        widget.configure(bg="lightblue")
    else:
        widget.configure(bg="SystemButtonFace")