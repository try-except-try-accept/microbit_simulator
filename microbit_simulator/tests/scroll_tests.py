from ..microbit import *


display.scroll("ABCDEFGH")


display.scroll("Hello, how are you?")


all_chars = "".join(chr(i) for i in range(32, 128))

display.scroll(all_chars)
