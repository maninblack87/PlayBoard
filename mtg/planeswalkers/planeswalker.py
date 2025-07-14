# planeswalkers/planeswalker.py

import planeswalkers.abilities

class Planeswalker:

    def __init__(self, name:str, max_hitpoint:int):
        self.name = name

        self.max_hitpoint = max_hitpoint
        self.current_hitpoint = max_hitpoint        # 현재 히트포인트 초기화

        self.energy_bonus = {"white":0, "red":0, "green":0, "blue":0, "black":0}
        self.abilities = {"ab1" : [0, []], "ab2" : [0, []], "ab3" : [0, []]}

    # 에너지 보너스 보정치 세팅 함수
    def set_energy_bonus(self, white_bonus, red_bonus, green_bonus, blue_bonus, black_bonus):
        self.energy_bonus["white"] = white_bonus
        self.energy_bonus["red"] = red_bonus
        self.energy_bonus["green"] = green_bonus
        self.energy_bonus["blue"] = blue_bonus
        self.energy_bonus["black"] = black_bonus

    # 어빌리티 세팅 함수
    def abilities(self, ab1_cost:int=None, ab1_list:list=None, ab2_cost:int=None, ab2_list:list=None, ab3_cost:int=None, ab3_list:list=None):
        self.abilities["ab1"] = [ab1_cost, ab1_list]
        self.abilities["ab2"] = [ab2_cost, ab2_list]
        self.abilities["ab3"] = [ab3_cost, ab3_list]

    # 히트포인트 감소 함수 <- 해당 함수가 필요하지 않을 수 있음
    def reduce_hitpoint(self, amount:int):
        self.current_hitpoint = self.current_hitpoint - amount
