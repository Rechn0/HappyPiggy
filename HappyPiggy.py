import time

import cv2


class HappyPiggy:
    def __init__(self):
        self.name = 'Harry Piggy'
        self.food_val = 100
        self.energy_val = 100
        self.state = 'normal'
        self.birth_time = time.strftime('%Y-%m-%d %H:%M:%S')

        self.state_frame_match = {
            "normal": [i + 1 for i in range(31)],
            "happy": [7, 8, 23, 24, 25, 8],
            "angry": [i for i in range(32, 54)],
            "shy": [54]
        }
        self.appearances = {
            "normal": list(),
            "happy": list(),
            "angry": list(),
            "shy": list()
        }
        for state in self.state_frame_match:
            self.__set_appearances(state)

    def __set_appearances(self, state):
        for i in self.state_frame_match.get(state):
            img = cv2.imread(f'Views/pigpic/{i}.png')
            h, w, g = img.shape
            frame = [[(img[x][y][2], img[x][y][1], img[x][y][0]) for y in range(w)] for x in range(h)]
            self.appearances[state].append(frame)

    def time_change_val(self):
        self.food_val -= 1
        self.energy_val -= 2

    def eat_change_val(self, val):
        self.food_val += val

    def sleep_change_val(self, sleep_time=1):
        self.energy_val += 20
