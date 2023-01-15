from ..microbit import *



import random

def wrap(x, y):
    """Wrap snake around matrix if it goes off edge"""
    if x == 5:
        x = 0
    elif x == -1:
        x = 4
    if y == 5:
        y = 0
    elif y == -1:
        y = 4
    
    return x, y

def move(x, y, direction):
    """Move head bit in current direction"""
    
    if direction == 'l':
        x -= 1
    elif direction == 'r':
        x += 1
    elif direction == 'u':
        y -= 1
    else:
        y += 1

    x, y = wrap(x, y)
    
    return [x, y]
    
def relocate_food(snake):
    """Find new random position for food that doesn't collide with snake"""
    found = False
    while not found:
        x, y = random.randint(0, 4), random.randint(0, 4)
        if [x, y] not in snake:
            found = True
            
    return [x, y]

def change_direction(button, direction):
    """Adjust current direction according to button"""
    
    ## if going right and B pressed, go down
    ## if going up and B pressed, go right
    ## if going down and B pressed, go right
    ## if going left and B pressed, go up
    
    ## if going left and A pressed, go down
    ## if going up and A pressed, go left
    ## if going down and A pressed, go left
    ## if going right and A pressed, go up
    
    if button == 'a':
        if direction == 'l':
            direction = 'd'
        elif direction == 'r':
            direction = 'u'
        elif direction == 'u':
            direction = 'l'
        elif direction == 'd':
            direction = 'l'
    elif button == 'b':
        if direction == 'l':
            direction = 'u'
        elif direction == 'r':
            direction = 'd'
        elif direction == 'u':
            direction = 'r'
        elif direction == 'd':
            direction = 'r'
            
    return direction

def check_eat_food(food, snake):
    """check if snake ate food"""
    if food in snake:
        return True
    else:
        return False
        
def check_game_over(snake):
    """Check game over - snake collided with self"""
    game_over = False
    
    for bit in snake:
        if snake.count(bit) > 1:
            game_over = True
            
    return game_over
        
def add_bit(snake, direction):
    """Add bit to snake as game gets harder"""
    x, y = snake[-1]
    if direction == 'r':
        x -= 1
    elif direction == 'l':
        x += 1
    elif direction == 'u':
        y -= 1
    else:
        y += 1
        
    x, y = wrap(x, y)
    
    snake.append([x,y])
    
    return snake
        
def score_point(food):
    """Display animation and add point when food eaten"""
    for b in range(9, -1, -1):
        display.set_pixel(food[0], food[1], b)
        sleep(5)

    display.scroll("NOM!", delay=40)

    return 1
        
## init snake position, direction of travel, speed (time delay), points,
## game over, timer, food location
snake = [[2,0], [1,0]]
direction = 'r'
speed = 300
points = 0
game_over = False
tick = 0
food = None

# main loop
while not game_over:
    display.clear()
    
    # display food
    if food is not None:
        
        display.set_pixel(food[0], food[1], 9)
            
        # check eat food
        if check_eat_food(food, snake):
            points += score_point(food)
            food = None
            tick = 0
                    
            # increase difficulty
            if points % 3 == 0:
                snake = add_bit(snake, direction)
                speed -= 25

    if button_a.was_pressed():
        direction = change_direction('a', direction)
    if button_b.was_pressed():
        direction = change_direction('b', direction)
        
    # remove tail piece
    head = snake.pop(-1)
    # add new head
    x, y = snake[0]
    new_head = move(x, y, direction)
    snake.insert(0, new_head)

    # display snake
    b = 7
    for x, y in snake:
        display.set_pixel(x, y, b)
        # glow head
        if len(snake) > 3:
            adjust = 1
        else:
            adjust = 2
            
        if b > 4:
            b -= adjust
        
    # relocate + hide food
    if tick == 25:
        food = relocate_food(snake)
        
    if tick == 50:
        food = None
        tick = 0
        
    # check snake collision
    game_over = check_game_over(snake)

    sleep(speed)
    # increment food timer
    tick += 1
    
display.scroll("GAME OVER! You scored: "+str(points), delay=100)
