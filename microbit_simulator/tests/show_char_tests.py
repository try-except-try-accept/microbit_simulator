from ..microbit import *

from random import randint



i = 32

while True:
    display.show(chr(i))
    sleep(500)
    i += 1
