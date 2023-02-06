from time import sleep as wait
from os import system
from pynput import keyboard
from datetime import datetime
import atexit
from config import *

last_button = ""
system("cls")

###################################################

class Image:

    HEART = [[0, 9, 0, 9, 0], [9, 9, 9, 9, 9], [9, 9, 9, 9, 9], [0, 9, 9, 9, 0], [0, 0, 9, 0, 0]]
    HEART_SMALL = [[0, 0, 0, 0, 0], [0, 9, 0, 9, 0], [0, 9, 9, 9, 0], [0, 0, 9, 0, 0], [0, 0, 0, 0, 0]]
    HAPPY = [[0, 0, 0, 0, 0], [0, 9, 0, 9, 0], [0, 0, 0, 0, 0], [9, 0, 0, 0, 9], [0, 9, 9, 9, 0]]
    SMILE = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [9, 0, 0, 0, 9], [0, 9, 9, 9, 0]]
    SAD = [[0, 0, 0, 0, 0], [0, 9, 0, 9, 0], [0, 0, 0, 0, 0], [0, 9, 9, 9, 0], [9, 0, 0, 0, 9]]
    CONFUSED = [[0, 0, 0, 0, 0], [0, 9, 0, 9, 0], [0, 0, 0, 0, 0], [0, 9, 0, 9, 0], [9, 0, 9, 0, 9]]
    ANGRY = [[9, 0, 0, 0, 9], [0, 9, 0, 9, 0], [0, 0, 0, 0, 0], [9, 9, 9, 9, 9], [9, 0, 9, 0, 9]]
    ASLEEP = [[0, 0, 0, 0, 0], [9, 9, 0, 9, 9], [0, 0, 0, 0, 0], [0, 9, 9, 9, 0], [0, 0, 0, 0, 0]]
    SURPRISED = [[0, 9, 0, 9, 0], [0, 0, 0, 0, 0], [0, 0, 9, 0, 0], [0, 9, 0, 9, 0], [0, 0, 9, 0, 0]]
    SILLY = [[9, 0, 0, 0, 9], [0, 0, 0, 0, 0], [9, 9, 9, 9, 9], [0, 0, 9, 0, 9], [0, 0, 9, 9, 9]]
    FABULOUS = [[9, 9, 9, 9, 9], [9, 9, 0, 9, 9], [0, 0, 0, 0, 0], [0, 9, 0, 9, 0], [0, 9, 9, 9, 0]]
    MEH = [[0, 9, 0, 9, 0], [0, 0, 0, 0, 0], [0, 0, 0, 9, 0], [0, 0, 9, 0, 0], [0, 9, 0, 0, 0]]
    YES = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 9], [0, 0, 0, 9, 0], [9, 0, 9, 0, 0], [0, 9, 0, 0, 0]]
    NO = [[9, 0, 0, 0, 9], [0, 9, 0, 9, 0], [0, 0, 9, 0, 0], [0, 9, 0, 9, 0], [9, 0, 0, 0, 9]]
    CLOCK12 = [[0, 0, 9, 0, 0], [0, 0, 9, 0, 0], [0, 0, 9, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    CLOCK11 = [[0, 9, 0, 0, 0], [0, 9, 0, 0, 0], [0, 0, 9, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    CLOCK10 = [[0, 0, 0, 0, 0], [9, 9, 0, 0, 0], [0, 0, 9, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    CLOCK9 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [9, 9, 9, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    CLOCK8 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 9, 0, 0], [9, 9, 0, 0, 0], [0, 0, 0, 0, 0]]
    CLOCK7 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 9, 0, 0], [0, 9, 0, 0, 0], [0, 9, 0, 0, 0]]
    CLOCK6 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 9, 0, 0], [0, 0, 9, 0, 0], [0, 0, 9, 0, 0]]
    CLOCK5 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 9, 0, 0], [0, 0, 0, 9, 0], [0, 0, 0, 9, 0]]
    CLOCK4 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 9, 0, 0], [0, 0, 0, 9, 9], [0, 0, 0, 0, 0]]
    CLOCK3 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 9, 9, 9], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    CLOCK2 = [[0, 0, 0, 0, 0], [0, 0, 0, 9, 9], [0, 0, 9, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    CLOCK1 = [[0, 0, 0, 9, 0], [0, 0, 0, 9, 0], [0, 0, 9, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    ARROW_N = [[0, 0, 9, 0, 0], [0, 9, 9, 9, 0], [9, 0, 9, 0, 9], [0, 0, 9, 0, 0], [0, 0, 9, 0, 0]]
    ARROW_NE = [[0, 0, 9, 9, 9], [0, 0, 0, 9, 9], [0, 0, 9, 0, 9], [0, 9, 0, 0, 0], [9, 0, 0, 0, 0]]
    ARROW_E = [[0, 0, 9, 0, 0], [0, 0, 0, 9, 0], [9, 9, 9, 9, 9], [0, 0, 0, 9, 0], [0, 0, 9, 0, 0]]
    ARROW_SE = [[9, 0, 0, 0, 0], [0, 9, 0, 0, 0], [0, 0, 9, 0, 9], [0, 0, 0, 9, 9], [0, 0, 9, 9, 9]]
    ARROW_S = [[0, 0, 9, 0, 0], [0, 0, 9, 0, 0], [9, 0, 9, 0, 9], [0, 9, 9, 9, 0], [0, 0, 9, 0, 0]]
    ARROW_SW = [[0, 0, 0, 0, 9], [0, 0, 0, 9, 0], [9, 0, 9, 0, 0], [9, 9, 0, 0, 0], [9, 9, 9, 0, 0]]
    ARROW_W = [[0, 0, 9, 0, 0], [0, 9, 0, 0, 0], [9, 9, 9, 9, 9], [0, 9, 0, 0, 0], [0, 0, 9, 0, 0]]
    ARROW_NW = [[9, 9, 9, 0, 0], [9, 9, 0, 0, 0], [9, 0, 9, 0, 0], [0, 0, 0, 9, 0], [0, 0, 0, 0, 9]]
    TRIANGLE = [[0, 0, 0, 0, 0], [0, 0, 9, 0, 0], [0, 9, 0, 9, 0], [9, 9, 9, 9, 9], [0, 0, 0, 0, 0]]
    TRIANGLE_LEFT = [[9, 0, 0, 0, 0], [9, 9, 0, 0, 0], [9, 0, 9, 0, 0], [9, 0, 0, 9, 0], [9, 9, 9, 9, 9]]
    CHESSBOARD = [[0, 9, 0, 9, 0], [9, 0, 9, 0, 9], [0, 9, 0, 9, 0], [9, 0, 9, 0, 9], [0, 9, 0, 9, 0]]
    DIAMOND = [[0, 0, 9, 0, 0], [0, 9, 0, 9, 0], [9, 0, 0, 0, 9], [0, 9, 0, 9, 0], [0, 0, 9, 0, 0]]
    DIAMOND_SMALL = [[0, 0, 0, 0, 0], [0, 0, 9, 0, 0], [0, 9, 0, 9, 0], [0, 0, 9, 0, 0], [0, 0, 0, 0, 0]]
    SQUARE = [[9, 9, 9, 9, 9], [9, 0, 0, 0, 9], [9, 0, 0, 0, 9], [9, 0, 0, 0, 9], [9, 9, 9, 9, 9]]
    SQUARE_SMALL = [[0, 0, 0, 0, 0], [0, 9, 9, 9, 0], [0, 9, 0, 9, 0], [0, 9, 9, 9, 0], [0, 0, 0, 0, 0]]
    RABBIT = [[9, 0, 9, 0, 0], [9, 0, 9, 0, 0], [9, 9, 9, 9, 0], [9, 9, 0, 9, 0], [9, 9, 9, 9, 0]]
    COW = [[9, 0, 0, 0, 9], [9, 0, 0, 0, 9], [9, 9, 9, 9, 9], [0, 9, 9, 9, 0], [0, 0, 9, 0, 0]]
    MUSIC_CROTCHET = [[0, 0, 9, 0, 0], [0, 0, 9, 0, 0], [0, 0, 9, 0, 0], [9, 9, 9, 0, 0], [9, 9, 9, 0, 0]]
    MUSIC_QUAVER = [[0, 0, 9, 0, 0], [0, 0, 9, 9, 0], [0, 0, 9, 0, 9], [9, 9, 9, 0, 0], [9, 9, 9, 0, 0]]
    MUSIC_QUAVERS = [[0, 9, 9, 9, 9], [0, 9, 0, 0, 9], [0, 9, 0, 0, 9], [9, 9, 0, 9, 9], [9, 9, 0, 9, 9]]
    PITCHFORK = [[9, 0, 9, 0, 9], [9, 0, 9, 0, 9], [9, 9, 9, 9, 9], [0, 0, 9, 0, 0], [0, 0, 9, 0, 0]]
    XMAS = [[0, 0, 9, 0, 0], [0, 9, 9, 9, 0], [0, 0, 9, 0, 0], [0, 9, 9, 9, 0], [9, 9, 9, 9, 9]]
    PACMAN = [[0, 9, 9, 9, 9], [9, 9, 0, 9, 0], [9, 9, 9, 0, 0], [9, 9, 9, 9, 0], [0, 9, 9, 9, 9]]
    TARGET = [[0, 0, 9, 0, 0], [0, 9, 9, 9, 0], [9, 9, 0, 9, 9], [0, 9, 9, 9, 0], [0, 0, 9, 0, 0]]
    TSHIRT = [[9, 9, 0, 9, 9], [9, 9, 0, 9, 9], [0, 9, 9, 9, 0], [0, 9, 9, 9, 0], [0, 9, 9, 9, 0]]
    ROLLERSKATE = [[0, 0, 0, 9, 9], [0, 0, 0, 9, 9], [9, 9, 9, 9, 9], [9, 9, 9, 9, 9], [0, 9, 0, 9, 0]]
    DUCK = [[0, 9, 9, 0, 0], [9, 9, 9, 0, 0], [0, 9, 9, 9, 9], [0, 9, 9, 9, 0], [0, 0, 0, 0, 0]]
    HOUSE = [[0, 0, 9, 0, 0], [0, 9, 9, 9, 0], [9, 9, 0, 9, 9], [0, 9, 0, 9, 0], [0, 9, 0, 9, 0]]
    TORTOISE = [[0, 0, 0, 0, 0], [0, 9, 9, 9, 0], [9, 9, 9, 9, 9], [0, 9, 0, 9, 0], [0, 0, 0, 0, 0]]
    BUTTERFLY = [[9, 9, 0, 9, 9], [9, 9, 9, 9, 9], [0, 0, 9, 0, 0], [9, 9, 9, 9, 9], [9, 9, 0, 9, 9]]
    STICKFIGURE = [[0, 0, 9, 0, 0], [9, 9, 9, 9, 9], [0, 0, 9, 0, 0], [0, 9, 0, 9, 0], [9, 0, 0, 0, 9]]
    GHOST = [[9, 9, 9, 9, 9], [9, 0, 9, 0, 9], [9, 9, 9, 9, 9], [9, 9, 9, 9, 9], [9, 0, 9, 0, 9]]
    SWORD = [[0, 0, 9, 0, 0], [0, 0, 9, 0, 0], [0, 0, 9, 0, 0], [0, 9, 9, 9, 0], [0, 0, 9, 0, 0]]
    GIRAFFE = [[9, 9, 0, 0, 0], [0, 9, 0, 0, 0], [0, 9, 0, 0, 0], [0, 9, 9, 9, 0], [0, 9, 0, 9, 0]]
    SKULL = [[0, 9, 9, 9, 0], [9, 0, 9, 0, 9], [9, 9, 9, 9, 9], [0, 9, 9, 9, 0], [0, 9, 9, 9, 0]]
    UMBRELLA = [[0, 9, 9, 9, 0], [9, 9, 9, 9, 9], [0, 0, 9, 0, 0], [9, 0, 9, 0, 0], [0, 9, 9, 0, 0]]
    SNAKE = [[9, 9, 0, 0, 0], [9, 9, 0, 9, 9], [0, 9, 0, 9, 0], [0, 9, 9, 9, 0], [0, 0, 0, 0, 0]]
    SCISSORS = [[0, 9, 0, 0, 9], [9, 9, 0, 9, 0], [9, 9, 9, 0, 0], [9, 9, 0, 9, 0], [0, 9, 0, 0, 9]]


    

        
    

class Button:
    """Re-implementation of the BBC micro:bit MicroPython Button class, interfacing with pynput"""
    def __init__(self, code):
        self.code = code
        self.pressed = False
        self.last_checked = datetime.now()
        self.tot_presses = 0
        self.last_pressed = datetime.now()
        

    def press(self):
        global last_button
        last_button = self.code        
        self.pressed = True
        self.tot_presses += 1
        self.last_pressed = datetime.now()

    def is_pressed(self):
        return self.pressed

    def was_pressed(self):
        if not self.last_pressed:
            return False
        
        was_pressed = False
        if self.last_pressed > self.last_checked:            
            was_pressed = True

        self.last_checked = datetime.now()
        
        return was_pressed

    def get_presses(self):
        num = self.tot_presses
        self.tot_presses = 0
        return num

###################################################

class Display:
    """Re-implementation of the BBC micro:bit MicroPython Display class for pixel emulation on the Windows terminal"""
    def __init__(self):
        self.clear()
        self.last_image = None
        self.last_out = ""
        
    def set_pixel(self, x, y, b):        
        self.leds[y][x] = b
        self.draw()

    def get_pixel(self, x, y):
        return self.leds[y][x]

    def show(self, img):
        self.clear()
        if len(img) == 1:
            img = char_to_led(img)
        self.leds = img
        self.draw()
        
    def scroll(self, string, delay=150, wait=True, loop=False, monospace=False): # TO DO - handle kwargs.
        self.leds = string_to_leds(string)

        while self.leds[0]:
            self.draw()
            sleep(delay)
            [self.leds[i].pop(0) for i in range(5)]
        self.clear()       

    def clear(self):
        self.leds = [[0 for i in range(DIM)] for j in range(DIM)]
        button_a.pressed = False
        button_b.pressed = False

    def hash(self, img):
        return "".join("".join(str(b) for b in row) for row in img) + last_button

    def draw(self):

        if self.hash(self.leds) != self.last_image:
        
            system("cls")
            out = ""
            for row in self.leds:
                for i in range(DIM):
                    led = 0
                    if i < len(row):
                        led = row[i]                
                    out += COLOURS[led] + " ██ "
                        
                out += "\n\n"
            print(out)
            self.last_out = out

        
        
            if last_button:
                if last_button == "B":
                    print()                    
                print(WHITE + f"button {last_button} was pressed")


            self.last_image = self.hash(self.leds)

###################################################

class MicrobitException(Exception):
    def __init__(self, err_msg):
        super().__init__(err_msg)

###################################################

def on_press(key):
    
    if key.char == "a": button_a.press()
    if key.char == "b": button_b.press()
    if key.char == "esc":   print(WHITE);   quit()


def char_to_led(char):
    return ALL_CHARS[ord(char)-32]

def string_to_leds(string):

    leds = [[] for i in range(5)]
    for char in string:
        char = char_to_led(char)        
        for i, row in enumerate(char):
            leds[i] += row

    return leds

def sleep(ms):
    wait(ms / 1000) # convert ms to seconds

def reset_console():
    print(WHITE)

###################################################

button_a = Button('A')
button_b = Button('B')
button_c = Button('C')
display = Display()

listener = keyboard.Listener(
    on_press=on_press,
    )
listener.start()

atexit.register(reset_console)
