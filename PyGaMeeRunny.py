import pygame
import time
import cv2
import random

from Food import Apple
from HappyPiggy import HappyPiggy
from Sounds import Sounds, sounds


class PyGaMeeRunny:
    def __init__(self, user):
        self.user = user
        self.happy_piggy = HappyPiggy()

        self.apple = Apple()

        self.val_chinglish_match = {
            "名字": 'name',
            "生日": 'birth_time',
            "饥饿值": 'food_val',
            "活力值": 'energy_val'
        }

        self.food_chinglish_match = {
            "苹果": 'apple'
        }

        self.screen_width = 1000
        self.screen_height = 500

        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
        self.screen.fill([255, 255, 255])
        self.pos = (0, 0)
        self.food_pos_x = self.screen_width / 2
        self.foos_pos_y = self.screen_height / 2
        self.food_angle = 60

        self.now = time.time()

        self.clock = pygame.time.Clock()
        # self.allow_move = True
        self.run = True

    def __show_piggy(self, state):
        pig = self.happy_piggy.appearances.get(state)[
            int(6 * time.time()) % len(self.happy_piggy.appearances.get(state))]

        di, dj = (random.randint(-4, 4), random.randint(-4, 4)) if state == "shy" else (0, 0)
        for i in range(len(pig)):
            for j in range(len(pig[i])):
                self.screen.set_at((2 * j + self.pos[0] - len(pig[i]) + dj, 2 * i + self.pos[1] - len(pig) + di),
                                   pig[i][j])
        pygame.display.update()
        return

    def __show_dialog(self, state, message=""):
        if message == "":
            return
        pig = self.happy_piggy.appearances.get(state)[
            int(6 * time.time()) % len(self.happy_piggy.appearances.get(state))]
        dialog_text = pygame.font.SysFont("SimHei", 20).render(message, True, (0, 0, 0))
        self.screen.blit(dialog_text, (self.pos[0] + len(pig[0]), self.pos[1] - len(pig)))
        return

    def __show_food(self, food_type, core: tuple, angle):
        food = self.__getattribute__(self.food_chinglish_match.get(food_type)).appearance
        image = pygame.transform.rotate(food, angle)
        self.screen.blit(image, image.get_rect(center=tuple(core)))

    def __show_val_info(self, val_type, val_x, val_y):
        show_info = f'{val_type}:{self.happy_piggy.__getattribute__(self.val_chinglish_match.get(val_type))}'
        info_text = pygame.font.SysFont("SimHei", 20).render(show_info, True, (0, 0, 0))
        self.screen.blit(info_text, (val_x, val_y))

    def __show_basic_info(self):
        show_info = f'{self.user}，你来看我啦! 扣1听我唱歌'
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
        shy_start_time = 0
        last_1_min = time.time()
        while self.run:
            # 处理事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.MOUSEMOTION:
                    self.pos = event.pos
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    shy_start_time = time.time()
                    sounds.yohu.play()
                elif event.type == pygame.KEYDOWN:
                    if event.key == ord('3') or event.key == ord('4'):
                        happy_start_time = time.time()
                        self.happy_piggy.eat_change_val(self.apple.food_val)
                        self.happy_piggy.sleep_change_val()
                        self.food_pos_x += 10
                        self.food_angle += 10
                        sounds.yohu.play()
                    elif event.key == ord('1'):
                        happy_start_time = time.time()
                        sounds.lalala.play()
                    elif event.key == ord('2'):
                        angry_start_time = time.time()

            self.now = time.time()
            if int(self.now - last_1_min) > 6:
                self.happy_piggy.time_change_val()
                last_1_min = self.now

            self.screen.fill([255, 255, 255])

            state = ""
            message = ""
            if int(self.now - shy_start_time) < 2:
                state = "shy"
                message = "QAQ"
            elif int(self.now - happy_start_time) < 5:
                state = "happy"
                message = "la~lala!"
            elif int(self.now - angry_start_time) < 5:
                state = "angry"
                message = "rua! rua rua!"
            else:
                state = "normal"

            self.__show_food(food_type="苹果", core=(self.food_pos_x, self.foos_pos_y), angle=self.food_angle)

            self.__show_piggy(state)
            self.__show_dialog(state, message)

            val_x, val_y = 0, 0
            for k in self.val_chinglish_match:
                self.__show_val_info(k, val_x, val_y)
                val_y += 50

            self.__show_basic_info()

            pygame.display.flip()
            self.clock.tick(20)
