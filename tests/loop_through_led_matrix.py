from microbit import *


speed = 1000
while True:

    for y in range(5):
        for x in range(5):
            display.set_pixel(x, y, 9)
            sleep(speed)
            
            
            speed -= 10

    display.clear()
