# unit_factory.py
from dragdrop_label import DragDropLabel

def create_unit(root, x, y, label_size, drop_callback, text="유닛", color="skyblue"):
    """
    root : 자식 위젯을 담는 부모 컨테이너
    x, y : 위젯이 생성되는 그리드 단위 위치 좌표
    label_size: 레이블의 픽셀 단위 크기
    drop_callback: 드래그 드랍의 드랍이 실행되었을때 호출되는 콜백함수
    """

    # 커스텀으로 드래그드랍이 되는 레이블을 생성
    unit = DragDropLabel(
        root,
        text=f"{text}",
        bg=color,
        relief="sunken",
        borderwidth=2,
        drop_callback=drop_callback
    )
    # 유닛이 생성되는 >>실제<< 위치
    px = x * label_size
    py = y * label_size

    # 유닛 배치 (위치와 크기)
    unit.place(
        x=px,
        y=py,
        width=label_size,
        height=label_size
    )

    # 시작 위치(원래 위치값) 갱신
    unit.origin_x = px
    unit.origin_y = py
    return unit
