from time import sleep as wait
from os import system

DIM = 5
MOD_RED_CHANNEL_ANSI = "\033[38;2;red;0;0m"
COLOURS = [MOD_RED_CHANNEL_ANSI.replace("red", str(i)) for i in range(0, 255, 25)]

ALL_CHARS = [[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
             [[0,9,0,0,0],[0,9,0,0,0],[0,9,0,0,0],[0,0,0,0,0],[0,9,0,0,0]],
             [[0,9,0,9,0],[0,9,0,9,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
             [[0,9,0,9,0,0],[9,9,9,9,9,0],[0,9,0,9,0,0],[9,9,9,9,9,0],[0,9,0,9,0,0]],
             [[0,9,9,9,0,0],[9,9,0,0,9,0],[0,9,9,9,9,0],[9,0,0,9,9,0],[0,9,9,9,0,0]],
             [[9,9,0,0,9,0],[9,0,0,9,0,0],[0,0,9,0,0,0],[0,9,0,0,9,0],[9,0,0,9,9,0]],
             [[0,9,9,0,0,0],[9,0,0,9,0,0],[0,9,9,0,0,0],[9,0,0,9,0,0],[0,9,9,0,9,0]],[[0,9,0],[0,9,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,9,0],[0,9,0,0],[0,9,0,0],[0,9,0,0],[0,0,9,0]],[[0,9,0,0],[0,0,9,0],[0,0,9,0],[0,0,9,0],[0,9,0,0]],[[0,0,0,0,0],[0,9,0,9,0],[0,0,9,0,0],[0,9,0,9,0],[0,0,0,0,0]],[[0,0,0,0,0],[0,0,9,0,0],[0,9,9,9,0],[0,0,9,0,0],[0,0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,9,0],[0,9,0,0]],[[0,0,0,0,0],[0,0,0,0,0],[0,9,9,9,0],[0,0,0,0,0],[0,0,0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,9,0],[0,0,0]],[[0,0,0,0,9,0],[0,0,0,9,0,0],[0,0,9,0,0,0],[0,9,0,0,0,0],[9,0,0,0,0,0]],[[0,9,9,0,0],[9,0,0,9,0],[9,0,0,9,0],[9,0,0,9,0],[0,9,9,0,0]],[[0,0,9,0,0],[0,9,9,0,0],[0,0,9,0,0],[0,0,9,0,0],[0,9,9,9,0]],[[9,9,9,0,0],[0,0,0,9,0],[0,9,9,0,0],[9,0,0,0,0],[9,9,9,9,0]],[[9,9,9,9,0],[0,0,0,9,0],[0,0,9,0,0],[9,0,0,9,0],[0,9,9,0,0]],[[0,0,9,9,0,0],[0,9,0,9,0,0],[9,0,0,9,0,0],[9,9,9,9,9,0],[0,0,0,9,0,0]],[[9,9,9,9,9,0],[9,0,0,0,0,0],[9,9,9,9,0,0],[0,0,0,0,9,0],[9,9,9,9,0,0]],[[0,0,0,9,0,0],[0,0,9,0,0,0],[0,9,9,9,0,0],[9,0,0,0,9,0],[0,9,9,9,0,0]],[[9,9,9,9,9,0],[0,0,0,9,0,0],[0,0,9,0,0,0],[0,9,0,0,0,0],[9,0,0,0,0,0]],[[0,9,9,9,0,0],[9,0,0,0,9,0],[0,9,9,9,0,0],[9,0,0,0,9,0],[0,9,9,9,0,0]],[[0,9,9,9,0,0],[9,0,0,0,9,0],[0,9,0,9,0,0],[0,0,9,0,0,0],[0,9,0,0,0,0]],[[0,0,0],[0,9,0],[0,0,0],[0,9,0],[0,0,0]],[[0,0,0,0],[0,0,9,0],[0,0,0,0],[0,0,9,0],[0,9,0,0]],[[0,0,0,9,0],[0,0,9,0,0],[0,9,0,0,0],[0,0,9,0,0],[0,0,0,9,0]],[[0,0,0,0,0],[0,9,9,9,0],[0,0,0,0,0],[0,9,9,9,0],[0,0,0,0,0]],[[0,9,0,0,0],[0,0,9,0,0],[0,0,0,9,0],[0,0,9,0,0],[0,9,0,0,0]],[[0,9,9,9,0,0],[9,0,0,0,9,0],[0,0,9,9,0,0],[0,0,0,0,0,0],[0,0,9,0,0,0]],[[0,9,9,9,0,0],[9,0,0,0,9,0],[9,0,9,0,9,0],[9,0,0,9,9,0],[0,9,9,0,0,0]],[[0,9,9,0,0],[9,0,0,9,0],[9,9,9,9,0],[9,0,0,9,0],[9,0,0,9,0]],[[9,9,9,0,0],[9,0,0,9,0],[9,9,9,0,0],[9,0,0,9,0],[9,9,9,0,0]],[[0,9,9,9,0],[9,0,0,0,0],[9,0,0,0,0],[9,0,0,0,0],[0,9,9,9,0]],[[9,9,9,0,0],[9,0,0,9,0],[9,0,0,9,0],[9,0,0,9,0],[9,9,9,0,0]],[[9,9,9,9,0],[9,0,0,0,0],[9,9,9,0,0],[9,0,0,0,0],[9,9,9,9,0]],[[9,9,9,9,0],[9,0,0,0,0],[9,9,9,0,0],[9,0,0,0,0],[9,0,0,0,0]],[[0,9,9,9,0,0],[9,0,0,0,0,0],[9,0,0,9,9,0],[9,0,0,0,9,0],[0,9,9,9,0,0]],[[9,0,0,9,0],[9,0,0,9,0],[9,9,9,9,0],[9,0,0,9,0],[9,0,0,9,0]],[[9,9,9,0],[0,9,0,0],[0,9,0,0],[0,9,0,0],[9,9,9,0]],[[9,9,9,9,9,0],[0,0,0,9,0,0],[0,0,0,9,0,0],[9,0,0,9,0,0],[0,9,9,0,0,0]],[[9,0,0,9,0],[9,0,9,0,0],[9,9,0,0,0],[9,0,9,0,0],[9,0,0,9,0]],[[9,0,0,0,0],[9,0,0,0,0],[9,0,0,0,0],[9,0,0,0,0],[9,9,9,9,0]],[[9,0,0,0,9,0],[9,9,0,9,9,0],[9,0,9,0,9,0],[9,0,0,0,9,0],[9,0,0,0,9,0]],[[9,0,0,0,9,0],[9,9,0,0,9,0],[9,0,9,0,9,0],[9,0,0,9,9,0],[9,0,0,0,9,0]],[[0,9,9,0,0],[9,0,0,9,0],[9,0,0,9,0],[9,0,0,9,0],[0,9,9,0,0]],[[9,9,9,0,0],[9,0,0,9,0],[9,9,9,0,0],[9,0,0,0,0],[9,0,0,0,0]],[[0,9,9,0,0],[9,0,0,9,0],[9,0,0,9,0],[0,9,9,0,0],[0,0,9,9,0]],[[9,9,9,0,0,0],[9,0,0,9,0,0],[9,9,9,0,0,0],[9,0,0,9,0,0],[9,0,0,0,9,0]],[[0,9,9,9,0],[9,0,0,0,0],[0,9,9,0,0],[0,0,0,9,0],[9,9,9,0,0]],[[9,9,9,9,9,0],[0,0,9,0,0,0],[0,0,9,0,0,0],[0,0,9,0,0,0],[0,0,9,0,0,0]],[[9,0,0,9,0],[9,0,0,9,0],[9,0,0,9,0],[9,0,0,9,0],[0,9,9,0,0]],[[9,0,0,0,9,0],[9,0,0,0,9,0],[9,0,0,0,9,0],[0,9,0,9,0,0],[0,0,9,0,0,0]],[[9,0,0,0,9,0],[9,0,0,0,9,0],[9,0,9,0,9,0],[9,9,0,9,9,0],[9,0,0,0,9,0]],[[9,0,0,9,0],[9,0,0,9,0],[0,9,9,0,0],[9,0,0,9,0],[9,0,0,9,0]],[[9,0,0,0,9,0],[0,9,0,9,0,0],[0,0,9,0,0,0],[0,0,9,0,0,0],[0,0,9,0,0,0]],[[9,9,9,9,0],[0,0,9,0,0],[0,9,0,0,0],[9,0,0,0,0],[9,9,9,9,0]],[[0,9,9,9,0],[0,9,0,0,0],[0,9,0,0,0],[0,9,0,0,0],[0,9,9,9,0]],[[9,0,0,0,0,0],[0,9,0,0,0,0],[0,0,9,0,0,0],[0,0,0,9,0,0],[0,0,0,0,9,0]],[[0,9,9,9,0],[0,0,0,9,0],[0,0,0,9,0],[0,0,0,9,0],[0,9,9,9,0]],[[0,0,9,0,0],[0,9,0,9,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[9,9,9,9,9,0]],[[0,9,0,0],[0,0,9,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0,0,0],[0,9,9,9,0,0],[9,0,0,9,0,0],[9,0,0,9,0,0],[0,9,9,9,9,0]],[[9,0,0,0,0],[9,0,0,0,0],[9,9,9,0,0],[9,0,0,9,0],[9,9,9,0,0]],[[0,0,0,0,0],[0,9,9,9,0],[9,0,0,0,0],[9,0,0,0,0],[0,9,9,9,0]],[[0,0,0,9,0],[0,0,0,9,0],[0,9,9,9,0],[9,0,0,9,0],[0,9,9,9,0]],[[0,9,9,0,0],[9,0,0,9,0],[9,9,9,0,0],[9,0,0,0,0],[0,9,9,9,0]],[[0,0,9,9,0],[0,9,0,0,0],[9,9,9,0,0],[0,9,0,0,0],[0,9,0,0,0]],[[0,9,9,9,0],[9,0,0,9,0],[0,9,9,9,0],[0,0,0,9,0],[0,9,9,0,0]],[[9,0,0,0,0],[9,0,0,0,0],[9,9,9,0,0],[9,0,0,9,0],[9,0,0,9,0]],[[0,9,0],[0,0,0],[0,9,0],[0,9,0],[0,9,0]],[[0,0,0,9,0],[0,0,0,0,0],[0,0,0,9,0],[0,0,0,9,0],[0,9,9,0,0]],[[9,0,0,0,0],[9,0,9,0,0],[9,9,0,0,0],[9,0,9,0,0],[9,0,0,9,0]],[[0,9,0,0,0],[0,9,0,0,0],[0,9,0,0,0],[0,9,0,0,0],[0,0,9,9,0]],[[0,0,0,0,0,0],[9,9,0,9,9,0],[9,0,9,0,9,0],[9,0,0,0,9,0],[9,0,0,0,9,0]],[[0,0,0,0,0],[9,9,9,0,0],[9,0,0,9,0],[9,0,0,9,0],[9,0,0,9,0]],[[0,0,0,0,0],[0,9,9,0,0],[9,0,0,9,0],[9,0,0,9,0],[0,9,9,0,0]],[[0,0,0,0,0],[9,9,9,0,0],[9,0,0,9,0],[9,9,9,0,0],[9,0,0,0,0]],[[0,0,0,0,0],[0,9,9,9,0],[9,0,0,9,0],[0,9,9,9,0],[0,0,0,9,0]],[[0,0,0,0,0],[0,9,9,9,0],[9,0,0,0,0],[9,0,0,0,0],[9,0,0,0,0]],[[0,0,0,0,0],[0,0,9,9,0],[0,9,0,0,0],[0,0,9,0,0],[9,9,0,0,0]],[[0,9,0,0,0,0],[0,9,9,9,0,0],[0,9,0,0,0,0],[0,9,0,0,0,0],[0,0,9,9,9,0]],[[0,0,0,0,0,0],[9,0,0,9,0,0],[9,0,0,9,0,0],[9,0,0,9,0,0],[0,9,9,9,9,0]],[[0,0,0,0,0,0],[9,0,0,0,9,0],[9,0,0,0,9,0],[0,9,0,9,0,0],[0,0,9,0,0,0]],[[0,0,0,0,0,0],[9,0,0,0,9,0],[9,0,0,0,9,0],[9,0,9,0,9,0],[9,9,0,9,9,0]],[[0,0,0,0,0],[9,0,0,9,0],[0,9,9,0,0],[0,9,9,0,0],[9,0,0,9,0]],[[0,0,0,0,0,0],[9,0,0,0,9,0],[0,9,0,9,0,0],[0,0,9,0,0,0],[9,9,0,0,0,0]],[[0,0,0,0,0],[9,9,9,9,0],[0,0,9,0,0],[0,9,0,0,0],[9,9,9,9,0]],[[0,0,9,9,0],[0,0,9,0,0],[0,9,9,0,0],[0,0,9,0,0],[0,0,9,9,0]],[[0,9,0],[0,9,0],[0,9,0],[0,9,0],[0,9,0]],[[9,9,0,0],[0,9,0,0],[0,9,9,0],[0,9,0,0],[9,9,0,0]],[[0,0,0,0,0],[0,0,0,0,0],[0,9,9,0,0],[0,0,0,9,9],[0,0,0,0,0]]]


for char in ALL_CHARS:

    if not all(len(row) == len(char[0]) for row in char):
        print("ERROR")
        print(char)

class MicrobitException(Exception):
    def __init__(self, err_msg):
        super().__init__(err_msg)


def char_to_led(char):
    return ALL_CHARS[ord(char)-32]

def string_to_leds(string):

    leds = [[] for i in range(5)]
    for char in string:
        char = char_to_led(char)        
        for i, row in enumerate(char):
            leds[i] += row

    return leds

class Display:
    def __init__(self):
        self.clear()
        
    def set_pixel(self, x, y, b):        
        self.leds[y][x] = b
        self.draw()

    def get_pixel(self, x, y):
        return self.leds[y][x]

    def show(self, img):
        self.clear()
        img = char_to_led(img)
        self.leds = img
        self.draw()
        

    def scroll(self, string, delay=150, wait=True, loop=False, monospace=False):
        self.leds = string_to_leds(string)

        while self.leds[0]:
            self.draw()
            sleep(delay)
            [self.leds[i].pop(0) for i in range(5)]
        


    def clear(self):
        self.leds = [0 for i in range(DIM ** 2)]

    def draw(self):       
        # brightness map for each pixel
        system("cls")
        out = ""
        for row in self.leds:
            for led in row[:5]:
                out += COLOURS[led] + " ██ "
            out += "\n\n"
        print(out)

        # decide what  colour to display
        pass

def sleep(ms):
    wait(ms / 1000) # convert ms to seconds


display = Display()


