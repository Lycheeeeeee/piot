from sense_hat import SenseHat
from time import sleep
class Emoji:
    sense = SenseHat()
    def __init__(self, e, m, f):
        self.eyes = e
        self.mouth = m
        self.face = f
    
    def display(self):
        e = self.eyes
        m = self.mouth
        f = self.face
        smilef_face = [
            f, f, f, f, f, f, f, f,
            f, f, f, f, f, f, f, f,
            f, e, e, f, f, e, e, f,
            f, e, e, f, f, e, e, f,
            f, f, f, f, f, f, f, f,
            f, m, m, f, f, m, m, f,
            f, f, f, m, m, f, f, f,
            f, f, f, f, f, f, f, f
            ]
    
        frowning_face =  [
            f, f, f, f, f, f, f, f,
            f, f, f, f, f, f, f, f,
            f, e, e, f, f, e, e, f,
            f, e, e, f, f, e, e, f,
            f, f, f, f, f, f, f, f,
            f, f, f, m, m, f, f, f,
            f, f, m, f, f, m, f, f,
            f, m, f, f, f, f, m, f
            ]

        freak_out = [
            f, f, f, f, f, f, f, f,
            f, f, f, f, f, f, f, f,
            f, e, e, f, f, e, e, f,
            f, e, e, f, f, e, e, f,
            f, f, f, f, f, f, f, f,
            f, m, f, m, f, m, f, f,
            f, f, m, f, m, f, m, f,
            f, f, f, f, f, f, f, f
            ]
        while True:
            self.sense.set_pixels(smilef_face)
            sleep(3)
            self.sense.set_pixels(frowning_face)
            sleep(3)
            self.sense.set_pixels(freak_out)
            sleep(3)

y = (255,255,0)
b = (0,0,0)
r = (255,0,0)
emoji = Emoji(y,r,b)
emoji.display()
