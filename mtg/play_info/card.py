class Card:

    def __init__(self, name:str, color:str="colorless", type=None, cost=None, dur:int=None, pow:int=None, evergreen=None, effect:str=None):
        self.name = name
        self.color = color
        self.type = type
        self.cost = cost
        self.dur = dur
        self.pow = pow
        self.evergreen = evergreen          # 추후 해당객체 추가예정
        self.effect = effect