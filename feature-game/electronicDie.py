from sense_hat import SenseHat
import random
import time

class eDie:
    # Symbolic initialization
    sense = SenseHat()
    
    # Setup the color
    d = [0, 0, 0]           # Default: Black
    g = [0, 255, 0]         # Green
    w = [255, 255, 255]     # White
    r = [255, 0, 0]         # Red
    o = [255, 165, 0]       # Orange
    y = [255, 255, 0]       # Yellow
    b = [0, 0, 255]         # Blue
    purple = [160, 32, 240] # Purple

    # Configure the dice on LED matrix
    # Player 1
    one_p1 = [
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,b,b,d,d,d,
    d,d,d,b,b,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    ]

    two_p1 = [
    d,d,d,d,d,d,d,d,
    d,b,b,d,d,d,d,d,
    d,b,b,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,b,b,d,
    d,d,d,d,d,b,b,d,
    d,d,d,d,d,d,d,d,
    ]

    three_p1 = [
    b,b,d,d,d,d,d,d,
    b,b,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,b,b,d,d,d,
    d,d,d,b,b,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,b,b,
    d,d,d,d,d,d,b,b,
    ]

    four_p1 = [
    d,d,d,d,d,d,d,d,
    d,b,b,d,d,b,b,d,
    d,b,b,d,d,b,b,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    d,b,b,d,d,b,b,d,
    d,b,b,d,d,b,b,d,
    d,d,d,d,d,d,d,d,
    ]

    five_p1 = [
    b,b,d,d,d,d,b,b,
    b,b,d,d,d,d,b,b,
    d,d,d,d,d,d,d,d,
    d,d,d,b,b,d,d,d,
    d,d,d,b,b,d,d,d,
    d,d,d,d,d,d,d,d,
    b,b,d,d,d,d,b,b,
    b,b,d,d,d,d,b,b,
    ]

    six_p1 = [
    b,b,d,d,d,d,b,b,
    b,b,d,d,d,d,b,b,
    d,d,d,d,d,d,d,d,
    b,b,d,d,d,d,b,b,
    b,b,d,d,d,d,b,b,
    d,d,d,d,d,d,d,d,
    b,b,d,d,d,d,b,b,
    b,b,d,d,d,d,b,b,
    ]

    # Player 2
    one_p2 = [
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,g,g,d,d,d,
    d,d,d,g,g,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    ]

    two_p2 = [
    d,d,d,d,d,d,d,d,
    d,g,g,d,d,d,d,d,
    d,g,g,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,g,g,d,
    d,d,d,d,d,g,g,d,
    d,d,d,d,d,d,d,d,
    ]

    three_p2 = [
    g,g,d,d,d,d,d,d,
    g,g,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,g,g,d,d,d,
    d,d,d,g,g,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,g,g,
    d,d,d,d,d,d,g,g,
    ]

    four_p2 = [
    d,d,d,d,d,d,d,d,
    d,g,g,d,d,g,g,d,
    d,g,g,d,d,g,g,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    d,g,g,d,d,g,g,d,
    d,g,g,d,d,g,g,d,
    d,d,d,d,d,d,d,d,
    ]

    five_p2 = [
    g,g,d,d,d,d,g,g,
    g,g,d,d,d,d,g,g,
    d,d,d,d,d,d,d,d,
    d,d,d,g,g,d,d,d,
    d,d,d,g,g,d,d,d,
    d,d,d,d,d,d,d,d,
    g,g,d,d,d,d,g,g,
    g,g,d,d,d,d,g,g,
    ]

    six_p2 = [
    g,g,d,d,d,d,g,g,
    g,g,d,d,d,d,g,g,
    d,d,d,d,d,d,d,d,
    g,g,d,d,d,d,g,g,
    g,g,d,d,d,d,g,g,
    d,d,d,d,d,d,d,d,
    g,g,d,d,d,d,g,g,
    g,g,d,d,d,d,g,g,
    ]

    @classmethod
    def die_roll(cls,player):
        
        # Generate random number from 1 to 6
        randomNumber = random.randint(1,6)
        
        if randomNumber == 1:
            if player == 1:
                cls.sense.set_pixels(cls.one_p1)
            elif player == 2:
                cls.sense.set_pixels(cls.one_p2)

        elif randomNumber == 2:
            if player == 1:
                cls.sense.set_pixels(cls.two_p1)
            elif player == 2:
                cls.sense.set_pixels(cls.two_p2)

        elif randomNumber == 3:
            if player == 1:
                cls.sense.set_pixels(cls.three_p1)
            elif player == 2:
                cls.sense.set_pixels(cls.three_p2)

        elif randomNumber == 4:
            if player == 1:
                cls.sense.set_pixels(cls.four_p1)
            elif player == 2:
                cls.sense.set_pixels(cls.four_p2)

        elif randomNumber == 5:
            if player == 1:
                cls.sense.set_pixels(cls.five_p1)
            elif player == 2:
                cls.sense.set_pixels(cls.five_p2)

        elif randomNumber == 6:
            if player == 1:
                cls.sense.set_pixels(cls.six_p1)
            elif player == 2:
                cls.sense.set_pixels(cls.six_p2)
                
        time.sleep(1)
        cls.sense.clear()        
        return(randomNumber)        

    @classmethod
    def checkMovement(cls,player):
        
             

            
        acceleration = cls.sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']

        x = abs(x)
        y = abs(y)
        z = abs(z)
        
        # Sensitivity to filter out accidental shakes
        if x > 1.2 or y > 1.2 or z > 1.2:            
            if player == 1:                
                result = eDie.die_roll(1)                 
                return result
            
            elif player == 2:                
                result = eDie.die_roll(2)                 
                return result          
        
        else:
            return eDie.checkMovement(player)            

    @classmethod
    def test(cls):
        
        cls.sense.set_pixels(cls.one_p1)

eDie.test()

