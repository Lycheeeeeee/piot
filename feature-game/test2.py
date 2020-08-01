from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
event = sense.stick.wait_for_event()
print(event.direction)
sleep(0.1)
event = sense.stick.wait_for_event()
print(event.direction)