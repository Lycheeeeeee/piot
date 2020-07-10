from sense_hat import SenseHat
import json
import time
from databaseConnection import MySQLConn
class Display:
    s = SenseHat()
    mysqlconn = MySQLConn()
    mydb = mysqlconn.conn
  
    mycursor = mysqlconn.cursor()

    green = (0, 255, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    temperature = s.get_temperature()
        
    OFFSET_LEFT = 1
    OFFSET_TOP = 2

    NUMS =[1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,  # 0
           0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,  # 1
           1,1,1,0,0,1,0,1,0,1,0,0,1,1,1,  # 2
           1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,  # 3
           1,0,0,1,0,1,1,1,1,0,0,1,0,0,1,  # 4
           1,1,1,1,0,0,1,1,1,0,0,1,1,1,1,  # 5
           1,1,1,1,0,0,1,1,1,1,0,1,1,1,1,  # 6
           1,1,1,0,0,1,0,1,0,1,0,0,1,0,0,  # 7
           1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,  # 8
           1,1,1,1,0,1,1,1,1,0,0,1,0,0,1]  # 9

# Displays a single digit (0-9)
    def show_digit(self,val, xd, yd, r, g, b):
        offset = val * 15
        for p in range(offset, offset + 15):
            xt = p % 3
            yt = (p-offset) // 3
            self.s.set_pixel(xt+xd, yt+yd, r*self.NUMS[p], g*self.NUMS[p], b*self.NUMS[p])

# Displays a two-digits positive number (0-99)
    def show_number(self,val, r, g, b):
        abs_val = abs(val)
        tens = abs_val // 10
        units = abs_val % 10
        if (abs_val > 9): 
            self.show_digit(tens, self.OFFSET_LEFT, self.OFFSET_TOP, r, g, b)
            self.show_digit(units, self.OFFSET_LEFT+4, self.OFFSET_TOP, r, g, b)
    def startDisplay(self):
        while True:
            if int(self.temperature ) <10:
                self.show_number(int(self.temperature),0,0,255)
            elif int(self.temperature)>= 10 and int(self.temperature)<=25:
                self.show_number(int(self.temperature),0,255,0)
            else:
                self.show_number(int(self.temperature),255,0,0)
display = Display()
display.startDisplay()
