import cv2
import pygame


class Food:
    def __init__(self, food_val: int, pic_path: str):
        self.food_val = food_val

        self.appearance = pygame.image.load(pic_path)


class Apple(Food):
    def __init__(self):
        super().__init__(10, 'Views/foodpic/apple.png')


class Banana(Food):
    pass
