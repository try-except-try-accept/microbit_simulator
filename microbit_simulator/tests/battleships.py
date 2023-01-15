
from ..microbit import *



##############################
### MicroBit Battleships #####
##############################
#### c.hall ### 2016 #########
##############################



def interlude():
    """Animation to seperate stages/messages"""
    display.clear()
    
    # light up matrix, column-by-column
    for x in range(0, 5):
        for y in range(0, 5):
            
            display.set_pixel(x, y, 9)
            sleep(70)
    
    # fade out matrix, led-by-led, beginning at bottom-right        
    for b in range(9, -1, -1):
        for x in range(4, -1, -1):
            for y in range(4, -1, -1):
                display.set_pixel(x, y, b)
                sleep(3)


def explode_ship_part(part, ships):
    """Flash pixel to signify damage to ship part"""
    for i in range(9, 0, -1):
        for x in range(i, 0, -1):
            display.set_pixel(part[0], part[1], x)
            sleep(100)
    
    #remove ship part from ship
    for ship in ships:
        if part in ship:
            ship.remove(part)
        #check if whole ship gone!
        if ship == []:
            display.scroll("Ship destroyed!", delay=80)
            ships.remove(ship)
            interlude()
            
            
            
def get_hit_selection(centre):
    """Gets LEDs around selecter to demonstrate selection"""
    selection = []
    
    for x in range(centre[0] - 1, centre[0] + 2):
        for y in range(centre[1] - 1, centre[1] + 2):
            if x > -1 and x < 5:
                if y > -1 and y < 5:
                    selection.append([x, y])
                    
    selection.remove(centre)
    return selection
    
def display_ships(ships):
    """Displays each ship with full brightness LEDs"""
    for ship in ships:
        for led in ship:
            display.set_pixel(led[0], led[1], 9)
    
    
def flash_selecter(selection, on):
    """Flashes LEDs around selecter to demonstrate selection"""
    if on:
        light = 5
    else:
        light = 0
    
    for x, y in selection:
        display.set_pixel(x, y, light)
    sleep(100)
    
def move_ship(selecter, length, vertical):
    """Moves ship NW -> SE around the matrix"""
    x = selecter[0]
    y = selecter[1]

    if not vertical:
        if x + length > 4:
            y += 1
            x = 0
        else:
            x += 1
        
        if y > 4:
            y = 0
    else:
        x += 1
        
        if x > 4:
            x = 0
            y += 1
            
        if y + length > 5:
            y = 0
    
    return [x, y]
    
def attempt_place(ships, selection):
    """Try and place ship, but check for collisions with already placed ships"""
    placed = True
    for ship in ships:
        for led in ship:
            if led in selection:
                placed = False
    
    if placed:
        ships.append(selection)
    
    return ships, placed
            


def check_hit(selecter, ships):
    """Check if target was HIT or MISS"""
    hit = False
    for ship in ships:
        if selecter in ship:
            hit = True
            
    if hit:
        display.scroll("HIT!")
        explode_ship_part(selecter, ships)
    else:
        display.scroll("MISS!")
        
    
            

def get_selection(selecter, length, vertical):
    """Find LEDs that match current position of selecter for current ship"""
    selection = []
    x = selecter[0]
    y = selecter[1]
    
    for i in range(length):
        if vertical:
            selection.append([x, y+i])
        else:
            selection.append([x+i, y])
            
    return selection
        
# introduction

while not button_b.was_pressed():
    msg = "BATTLESHIPS press B to begin"
    display.scroll(msg, delay=70)

interlude()

msg = 'select starting locations A:ROTATE B:MOVE A+B:PLACE'
display.scroll(msg, delay=90)
interlude()

ships = []
options = {"BATTLESHIP":3,
            "SUBMARINE":2,
            "DESTROYER":1}

for ship in options.keys():
    
    placed = False
    vertical = False
    selecter = [0,0]

    display.scroll("place " + ship, delay=70)
    
    selection = get_selection(selecter, options[ship], vertical)
    
    while not placed:
        
        flash_selecter(selection, True)
        
        display.clear()
        display_ships(ships)
        
        
        
        
        if button_b.is_pressed() and button_a.is_pressed():
            ships, placed = attempt_place(ships, selection)
        elif button_b.is_pressed():
            selecter = move_ship(selecter, options[ship], vertical)
            selection = get_selection(selecter, options[ship], vertical)
        elif button_a.is_pressed():
            if vertical:
                vertical = False
            else:
                vertical = True
            selecter = move_ship(selecter, options[ship], vertical)
            selection = get_selection(selecter, options[ship], vertical)            
            
        
        flash_selecter(selection, False)
    
interlude()
msg = "READY? Select target blocks"

display.scroll(msg, delay=90)
interlude()

## play game loop


selecter = [0, 0]
while len(ships) > 0:
    selection = get_hit_selection(selecter)
    flash_selecter(selection, True)
    
    display.clear()
    
    display_ships(ships)
    
    if button_b.is_pressed():
        selecter = move_ship(selecter, 1, False)
    
    if button_a.is_pressed():
        check_hit(selecter, ships)
        selecter = [0, 0]
        
    flash_selecter(selection, False)

interlude()
display.scroll("YOU LOSE! :(", delay=100)
interlude()



