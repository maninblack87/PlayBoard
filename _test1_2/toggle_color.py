colors = ["white", "lightblue", "lightgreen", "yellow", "pink", "orange"]

color_index_map = {}

def toggle_color(event):

    widget = event.widget
    widget_id = str(widget)
    current_index = color_index_map.get(widget_id, 0)
    next_index = (current_index + 1) % len(colors)
    widget.configure(bg=colors[next_index])
    color_index_map[widget_id] = next_index