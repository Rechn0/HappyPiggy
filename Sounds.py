from pygame import mixer


class Sounds:
    def __init__(self):
        mixer.init()
        self.lalala = mixer.Sound("./Sounds/lalala.wav")
        self.yohu = mixer.Sound("./Sounds/yohu.wav")


sounds = Sounds()
