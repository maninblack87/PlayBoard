colors = ["SystemButtonFace", "lightblue", "lightgreen", "yellow", "pink", "orange"]

color_index_map = {}

def toggle_color(event):

    widget = event.widget
    widget_id = str(widget)

    # 인덱스 카운팅
    # 초기의 current_index = 0
    # next_index가 0->1->2->3->4->5->0
    current_index = color_index_map.get(widget_id, 0)
    next_index = (current_index + 1) % len(colors)