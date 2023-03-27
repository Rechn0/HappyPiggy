import time


class HappyPiggy:
    def __init__(self):
        self.name = 'Harry Piggy'
        self.food_val = 100
        self.energy_val = 100
        self.state = 'normal'
        self.birth_time = time.strftime('%Y-%m-%d %H:%M:%S')

    def time_change_val(self):
        self.food_val -= 1
        self.energy_val -= 2

    def eat_change_val(self,food_type=1):
        self.food_val += 10

    def sleep_change_val(self, sleep_time=1):
        self.energy_val += 20
