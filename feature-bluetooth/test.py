from sense_hat import SenseHat


w = [255, 255, 255]     # White
b = [0, 0, 255]         # Blue

bluetooth_icon = [
    b,b,b,w,b,b,b,b,
    b,w,b,w,w,b,b,b,
    b,b,w,w,b,w,b,b,
    b,b,b,w,w,b,b,b,
    b,b,b,w,w,b,b,b,
    b,b,w,w,b,w,b,b,
    b,w,b,w,w,b,b,b,
    b,b,b,w,b,b,b,b,
]

sense = SenseHat()
# sense.set_pixels(bluetooth_icon)
# time.sleep(2)
sense.clear()