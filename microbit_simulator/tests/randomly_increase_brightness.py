from ..microbit import *

from random import randint

while True:


    x = randint(0, 4)
    y = randint(0, 4)

    brightness = display.get_pixel(x, y)

    brightness += 1

    display.set_pixel(x, y, brightness)

    sleep(100)
    
