colors = ['SystemButtonFace', 'lightblue', 'lightgreen', 'yellow', 'pink', 'orange']

color_index_map = {}

def toggle_color(event):
    
    # 이벤트가 발생한 위젯(이하 해당위젯)을 저장
    widget = event.widget

    current_index = color_index_map.get(str(widget), 0)
    next_index = (current_index + 1) % len(colors)

    # 해당위젯의 옵션중 색상(bg) 변경 적용
    widget.configure(bg=colors[next_index])

    # 변경된 위젯의 정보 별도 딕셔너리(color_index_map)에 저장
    color_index_map[str(widget)] = next_index
