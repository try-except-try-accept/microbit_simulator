from time import sleep as wait
from os import system

DIM = 5
MOD_RED_CHANNEL_ANSI = "\033[38;2;red;0;0m"
COLOURS = [MOD_RED_CHANNEL_ANSI.replace("red", str(i)) for i in range(0, 255, 25)]


class Display:
    def __init__(self):
        self.clear()
        
    def set_pixel(self, x, y, b):        
        self.leds[(y * DIM) + x] = b
        self.draw()

    def show(self, img):
        self.draw()

    def scroll(self):
        self.draw()

    def clear(self):
        self.leds = [0 for i in range(DIM ** 2)]

    def draw(self):       
        # brightness map for each pixel
        system("cls")
        out = ""
        for i, led in enumerate(self.leds):
            out += COLOURS[led] + " ██ "

            if i > 0 and i+1 < DIM ** 2 and (i+1) % DIM == 0:
                out += "\n\n"
                

        print(out)

        # decide what  colour to display
        pass

def sleep(ms):
    wait(ms / 1000) # convert ms to seconds


display = Display()


