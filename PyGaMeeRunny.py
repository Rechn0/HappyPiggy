import pygame
import time

from HappyPiggy import HappyPiggy


class PyGaMeeRunny:
    def __init__(self):
        self.happy_piggy = HappyPiggy()
        self.state_txt_match = {
            "normal": "123456",
            "happy": "57"
        }

        self.val_chinglish_match = {
            "名字": 'name',
            "生日": 'birth_time',
            "饥饿值": 'food_val',
            "活力值": 'energy_val'
        }

        self.appearances = {
            "normal": list(),
            "happy": list(),
            "angry": list()
        }
        for state in self.state_txt_match:
            self.__set_appearances(state)

        self.screen = pygame.display.set_mode([1000, 500])
        self.screen.fill([255, 255, 255])
        self.pos = (0, 0)

        self.now = time.time()

        self.clock = pygame.time.Clock()

        self.run = True

    def __set_appearances(self, state):
        for i in self.state_txt_match.get(state):
            frame = list()
            with open(f'{i}.txt', 'r') as f:
                for line in f.readlines():
                    frame.append(line)
            self.appearances[state].append(frame)

    def __show_piggy(self, state):
        pig = self.appearances.get(state)[int(2 * time.time()) % len(self.appearances.get(state))]
        self.screen.fill([255, 255, 255])
        for i in range(len(pig)):
            for j in range(len(pig[i])):
                if pig[i][j] in 'M\n':
                    continue
                self.screen.set_at((2 * j + self.pos[0] - len(pig[i]), 4 * i + self.pos[1] - len(pig)), (0, 0, 0))

    def __show_val_info(self, type, val_x, val_y):
        show_info = f'{type}:{self.happy_piggy.__getattribute__(self.val_chinglish_match.get(type))}'
        info_text = pygame.font.SysFont("SimHei", 20).render(show_info, True, (0, 0, 0))
        self.screen.blit(info_text, (val_x, val_y))

    def __eat(self, food_kind):
        pass

    def __sleep(self):
        pass

    def __angry(self):
        pass

    def __hungry(self):
        self.screen.fill([255, 255, 255])
        self.__angry()

    def running(self):
        global happy_start_time
        global last_1_min
        happy_start_time = 0
        last_1_min = time.time()
        while self.run:
            # 处理事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.MOUSEMOTION:
                    self.pos = event.pos
                elif event.type == pygame.KEYDOWN:
                    if event.key == ord('a') or event.key == ord('b'):
                        happy_start_time = time.time()
                        self.happy_piggy.eat_change_val()
                        self.happy_piggy.sleep_change_val()

            self.now = time.time()
            if int(self.now - last_1_min) > 6:
                self.happy_piggy.time_change_val()
                last_1_min = self.now

            if int(self.now - happy_start_time) < 5:
                self.__show_piggy("happy")
            else:
                self.__show_piggy("normal")

            val_x, val_y = 0, 0
            for k in self.val_chinglish_match:
                self.__show_val_info(k, val_x, val_y)
                val_y += 50

            pygame.display.flip()
            self.clock.tick(20)
