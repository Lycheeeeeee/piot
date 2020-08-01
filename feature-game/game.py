from sense_hat import SenseHat
import time

from datetime import datetime
from electronicDie import eDie
from writeToCsv import csvHandler

class Game:
    # Symbolic initialization
    sense = SenseHat()
    continued = True
    instruction_show = True
    p1_turn_toggle = True
    p2_turn_toggle = True
    p1 = 0  # Player score
    p2 = 0
    counter_p1 = 0  # Player turn counter
    counter_p2 = 0
    winner = 0      # Winner variables
    winner_score = 0
    winner_turns = 0

    # Setup the color
    black = [0, 0, 0]       # Black
    g = [0, 255, 0]         # Green
    w = [255, 255, 255]     # White
    r = [255, 0, 0]         # Red
    o = [255, 165, 0]       # Orange
    y = [255, 255, 0]       # Yellow
    b = [0, 0, 255]         # Blue
    purple = [160, 32, 240] # Purple
    
    # Introduce the game
    @classmethod
    def showIntro(cls):
        # cls.sense.show_message("Welcome!", text_colour=cls.w, back_colour=cls.r,\
        #      scroll_speed=0.05)
        # time.sleep(0.5)
        # cls.sense.show_message("shake the Pi and get 30 first to win", \
        #     text_colour=cls.w, back_colour=cls.r, scroll_speed=0.05)
        
        # time.sleep(0.5)
        # cls.sense.show_message("use joystick to select", \
        #     text_colour=cls.w, back_colour=cls.r, scroll_speed=0.05)
        cls.sense.show_message("<< P1 <<", text_colour=cls.b, scroll_speed=0.05)        
        cls.sense.show_message(">> P2 >>", text_colour=cls.g, scroll_speed=0.05)

        time.sleep(0.5)
        cls.sense.show_message("GO!",text_colour=cls.w, back_colour=cls.r, scroll_speed=0.05)
        
        cls.sense.clear()
        cls.startGame()

    # When player 1 toggles left joystick
    @classmethod
    def left_pushed(cls,event):
        
        # Player pressed and released the joystick      
        if event[2] == "released":            
            cls.sense.show_message("P1", text_colour=cls.b, scroll_speed = 0.02)                 
            time.sleep(0.05)
            result = eDie.checkMovement(1)
            # If the player shakes the dice
            if result != None:
                cls.counter_p1 += 1
                cls.p1 += result               
            else:
                cls.right_pushed(event)
            # If the player reaches 30 first
            if cls.p1 > 10:
                cls.winner = 1
                cls.winner_score = cls.p1
                cls.winner_turns = cls.counter_p1
                cls.continued = False
        cls.sense.clear()

    # When player 2 toggles right joystick
    @classmethod
    def right_pushed(cls,event):                
        # Player pressed and released the joystick
        if event[2] == "released":
            # while cls.p1_turn_toggle:
            cls.sense.show_message("P2", text_colour=cls.g, scroll_speed = 0.02)           
            time.sleep(0.05)            
            result = eDie.checkMovement(2)
            # If the player shakes the dice           
            if result != None:                                
                cls.counter_p2 += 1
                cls.p2 += result
            else:
                cls.right_pushed(event)

            # If the player reaches 30 first
            if cls.p2 > 10:
                cls.winner = 2
                cls.winner_score = cls.p2
                cls.winner_turns = cls.counter_p2
                cls.continued = False
        cls.sense.clear()

    @classmethod
    def startGame(cls):   
        cls.sense.stick.direction_left = cls.left_pushed
        cls.sense.stick.direction_right = cls.right_pushed

        # Continue the game till stop trigger
        while cls.continued:
            pass
         
        print("Player 1: {} in {}".format(cls.p1, cls.counter_p1))
        print("Player 2: {} in {}".format(cls.p2, cls.counter_p2))       

        # Acknowledge the winner        
        cls.sense.show_message("Player {} wins".format(cls.winner), back_colour=cls.r,\
            scroll_speed=0.05)

        cls.sense.clear()
        
        result_message = "Player {} wins with {} points in {} turns"\
            .format(cls.winner, cls.winner_score, cls.winner_turns)
        
        # Write to csv file
        csvHandler.writeToCsv(result_message)
                
# Start the program
Game.showIntro()
