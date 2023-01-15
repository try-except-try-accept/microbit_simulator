from ..microbit import *

from random import randint



i = 32

while i < 127:
    display.show(chr(i))
    sleep(400)
    i += 1
    display.clear()
    sleep(100)
