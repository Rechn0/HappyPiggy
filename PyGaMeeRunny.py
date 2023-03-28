import pygame
import time
import cv2

from HappyPiggy import HappyPiggy


class PyGaMeeRunny:
    def __init__(self, user):
        self.user = user
        self.happy_piggy = HappyPiggy()

        self.val_chinglish_match = {
            "名字": 'name',
            "生日": 'birth_time',
            "饥饿值": 'food_val',
            "活力值": 'energy_val'
        }

        self.screen_width = 1000
        self.screen_height = 500

        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
        self.screen.fill([255, 255, 255])
        self.pos = (0, 0)

        self.now = time.time()

        self.clock = pygame.time.Clock()

        self.run = True

    def __show_piggy(self, state):
        pig = self.happy_piggy.appearances.get(state)[
            int(6 * time.time()) % len(self.happy_piggy.appearances.get(state))]
        self.screen.fill([255, 255, 255])
        for i in range(len(pig)):
            for j in range(len(pig[i])):
                self.screen.set_at((2 * j + self.pos[0] - len(pig[i]), 2 * i + self.pos[1] - len(pig)), pig[i][j])
        pygame.display.update()
        return

    def __show_val_info(self, type, val_x, val_y):
        show_info = f'{type}:{self.happy_piggy.__getattribute__(self.val_chinglish_match.get(type))}'
        info_text = pygame.font.SysFont("SimHei", 20).render(show_info, True, (0, 0, 0))
        self.screen.blit(info_text, (val_x, val_y))

    def __show_basic_info(self):
        show_info = f'{self.user}，你来看我啦!'
        info_text = pygame.font.SysFont("SimHei", 30).render(show_info, True, (0, 128, 128))
        self.screen.blit(info_text, (self.screen_width / 2, 0))

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
        global happy_start_time, msg, last_1_min
        global happy_start_time
        global angry_start_time
        global last_1_min
        happy_start_time = 0
        angry_start_time = 0
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
                    elif event.key == ord('1'):
                        happy_start_time = time.time()
                    elif event.key == ord('2'):
                        angry_start_time = time.time()

            self.now = time.time()
            if int(self.now - last_1_min) > 6:
                self.happy_piggy.time_change_val()
                last_1_min = self.now

            if int(self.now - happy_start_time) < 5:
                self.__show_piggy("happy")
            elif int(self.now - angry_start_time) < 5:
                self.__show_piggy("angry")
            else:
                self.__show_piggy("normal")

            val_x, val_y = 0, 0
            for k in self.val_chinglish_match:
                self.__show_val_info(k, val_x, val_y)
                val_y += 50

            self.__show_basic_info()

            pygame.display.flip()
            self.clock.tick(20)
