import cv2


class Food:
    def __init__(self, food_val: int, pic_path: str):
        self.food_val = food_val
        img = cv2.imread(pic_path)
        h, w, g = img.shape
        self.appearance = [[(img[x][y][2], img[x][y][1], img[x][y][0]) for y in range(w)] for x in range(h)]


class Apple(Food):
    def __init__(self):
        super().__init__(10, 'Views/foodpic/apple.png')


class Banana(Food):
    pass
