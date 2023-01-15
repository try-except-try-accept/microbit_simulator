from ..microbit import *



while True:

    for y in range(5):
        for x in range(5):

            display.set_pixel(x, y, 9)
            sleep(100)            

    display.clear()
