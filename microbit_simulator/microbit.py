from time import sleep as wait
from os import system
from pynput import keyboard
from datetime import datetime
import atexit
from config import *

###################################################

class Image:

    HEART = '''01010
11111
11111
01110
00100'''
    PACMAN = '''01111
11010
11100
11110
01111'''
    

class Button:
    """Re-implementation of the BBC micro:bit MicroPython Button class, interfacing with pynput"""
    def __init__(self):
        self.pressed = False
        self.last_checked = datetime.now()
        self.tot_presses = 0
        self.last_pressed = datetime.now()        

    def press(self):
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
        
    def set_pixel(self, x, y, b):        
        self.leds[y][x] = b
        self.draw()

    def get_pixel(self, x, y):
        return self.leds[y][x]

    def show(self, img):
        self.clear()
        if set(img) != {'1', '0'}:
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

    def draw(self):       
        
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

button_a = Button()
button_b = Button()
display = Display()
          

listener = keyboard.Listener(
    on_press=on_press,
    )
listener.start()

atexit.register(reset_console)
