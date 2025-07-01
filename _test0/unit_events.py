# unit_events.py
from unit_factory import create_unit

def spawn_unit(event, root, x, y, label_size, drop_callback):
    unit_number = (y - 4) * 8 + x + 1  # 유닛 슬롯 번호 계산
    create_unit(root, x, y, label_size, drop_callback, text=f"유닛 {unit_number}")