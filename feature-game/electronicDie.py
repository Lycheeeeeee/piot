from sense_hat import SenseHat
import random
import time

sense = SenseHat()
b = [0, 0, 0]
g = [0, 255, 0]
r = [255, 0, 0]

# Configure the dice on LED matrix
one = [
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,r,r,b,b,b,
b,b,b,r,r,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
]

two = [
b,b,b,b,b,b,b,b,
b,r,r,b,b,b,b,b,
b,r,r,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,r,r,b,
b,b,b,b,b,r,r,b,
b,b,b,b,b,b,b,b,
]

three = [
r,r,b,b,b,b,b,b,
r,r,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,r,r,b,b,b,
b,b,b,r,r,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,r,r,
b,b,b,b,b,b,r,r,
]

four = [
b,b,b,b,b,b,b,b,
b,r,r,b,b,r,r,b,
b,r,r,b,b,r,r,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,r,r,b,b,r,r,b,
b,r,r,b,b,r,r,b,
b,b,b,b,b,b,b,b,
]

five = [
r,r,b,b,b,b,r,r,
r,r,b,b,b,b,r,r,
b,b,b,b,b,b,b,b,
b,b,b,r,r,b,b,b,
b,b,b,r,r,b,b,b,
b,b,b,b,b,b,b,b,
r,r,b,b,b,b,r,r,
r,r,b,b,b,b,r,r,
]

six = [
r,r,b,b,b,b,r,r,
r,r,b,b,b,b,r,r,
b,b,b,b,b,b,b,b,
r,r,b,b,b,b,r,r,
r,r,b,b,b,b,r,r,
b,b,b,b,b,b,b,b,
r,r,b,b,b,b,r,r,
r,r,b,b,b,b,r,r,
]

# randomNumber = 0

class eDie:
    
    @staticmethod
    def die_roll():

        randomNumber = random.randint(1,6)
        
        if randomNumber == 1:
            sense.set_pixels(one)
        elif randomNumber == 2:
            sense.set_pixels(two)
        elif randomNumber == 3:
            sense.set_pixels(three)
        elif randomNumber == 4:
            sense.set_pixels(four)
        elif randomNumber == 5:
            sense.set_pixels(five)
        elif randomNumber == 6:
            sense.set_pixels(six)
        time.sleep(1)
        sense.clear()
        # print("Return " + str(type(randomNumber)))
        # print("return + " + str(randomNumber))
        print(str(randomNumber))
        return(randomNumber)
        
        

    @staticmethod
    def checkMovement():
        
        # while True:
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']

        x = abs(x)
        y = abs(y)
        z = abs(z)

        if x > 1.2 or y > 1.2 or z > 1.2:
            return eDie.die_roll()
        else:
            # print("no movement")
            sense.clear()