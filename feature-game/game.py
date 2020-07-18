from sense_hat import SenseHat
import time
from electronicDie import eDie

sense = SenseHat()
# Setup the color
g = [0, 255, 0]
w = [255, 255, 255]  # White
r = [255, 0, 0] # Red
o = [255, 165, 0]
y = [255, 255, 0]
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (160, 32, 240)

# Introduce the game
def showIntro():
    # sense.show_message("Welcome!")
    # sense.show_message("P1", text_colour=blue, back_colour=y)
    # sense.show_message("vs")
    # sense.show_message("P2", text_colour=green, back_colour=r)
    # sense.show_message("Get30FirstToWin")
    # sense.show_message("GO!",text_colour=r,back_colour=y)
    # time.sleep(1)
    # sense.clear()
    startGame()
    

# P1 play
def startGame():
    print("Game started")
    counter = 0
    attempts = 0
    player = 1
    # Players' score based on attempts
    p1 = 0
    p2 = 0
    # Player 1's turn
    sense.show_message("P1", text_colour=blue, back_colour=y)
    
    # Game logic
    while True:
        # print("play")
        dieResult = eDie.checkMovement()
        
        # everytime player shakes the die
        if dieResult != None:
            counter += dieResult
            attempts += 1
            if counter > 5 and player == 1:
                print("P1 got " + str(counter) 
                + " in " + str(attempts) + " attempts")
                
                # Assign score for p1
                p1 = attempts

                # Reset the values for P2
                counter = 0
                attempts = 0
                player = 2

                # Player 2's turn
                sense.show_message("P2", text_colour=green, back_colour=r)
                sense.clear()

            elif counter > 5 and player == 2:
                print("P2 got " + str(counter) 
                + " in " + str(attempts) + " attempts")
    
                # Assign score for P2
                p2 = attempts
                break

    if p1 == p2:
        print("Tie, Play Again")
        sense.show_message("TIE", text_colour=purple)
        startGame()
    else:
        if p1 < p2:
            print("P1 wins")
            sense.show_message("P1 WINS", text_colour=blue, back_colour=y)
        elif p1 > p2:
            print("P2 wins")
            sense.show_message("P2 WINS", text_colour=green, back_colour=r)
        print("Game Over, saving score")
        sense.clear() 
              
# Start the program
showIntro()
