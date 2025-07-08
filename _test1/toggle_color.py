colors = ["SystemButtonFace", "lightblue", "lightgreen", "yellow", "pink", "orange"]

color_index_map = {}

def toggle_color(event):

    # 이벤트가 발생한 위젯을 저장
    widget = event.widget

    # 이벤트 발생전 위젯의 상태를 기억하고 불러오기 위해(선택된 위젯의 이름)
    widget_id = str(widget)

    # 테스트
    print("\nwidget_id : " + widget_id)

    # 현재 인덱스를 정의한다 : widget_id에 해당하는 값을 꺼내거나, 없다면 0을 반환한다
    current_index = color_index_map.get(widget_id, 0)

    # 테스트
    print("current_index : " + str(current_index))

    # 테스트
    print("색상적용 전: " + str(color_index_map))

    # 다음 인덱스로 순환하기위한 수식
    next_index = (current_index + 1) % len(colors)

    # 테스트
    print("next_index : " + str(next_index))

    # 색상 적용
    widget.configure(bg=colors[next_index])

    # 인덱스 저장 : widget_id의 키를 저장
    color_index_map[widget_id] = next_index

    # 테스트
    print("색상적용 후 : " + str(color_index_map))