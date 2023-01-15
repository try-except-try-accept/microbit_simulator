from ..microbit import *


while True:

    if button_a.is_pressed():

        break

    display.scroll("Stuff")

    if button_b.was_pressed():

        display.scroll(f"Button b pressed {button_b.get_presses()} times!")

    
