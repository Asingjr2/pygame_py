"""Creating box with square that changes color and moves.  

Link can be tutorial link can be found at: https://nerdparadise.com/programming/pygame/part1
"""
import pygame as game

# Initializes program
game.init()
# Set screen size (width, length)
screen = game.display.set_mode((600, 600))
# constant variable for running game
done = False
# Used to change color with key down later
is_blue = True
# Variable used to set surface object size
x = 30
y = 30

# Time used to slow down processing (below example uses 60 frames a sec)
clock = game.time.Clock()

while not done:
    for event in game.event.get():
        if event.type == game.QUIT:
            done = True
        
        if event.type == game.KEYDOWN and event.key == game.K_SPACE:
            is_blue = not is_blue

        # Standard term for creating key shorcut and then results of each press
        pressed = game.key.get_pressed()

        if pressed[game.K_UP]:
            y -=3
        if pressed[game.K_DOWN]:
            y += 3
        if pressed[game.K_LEFT]:
            x -= 3
        if pressed[game.K_RIGHT]:
            x += 3
        # Creating exaggerated move
        if pressed[game.K_l]:
            x += 300

        screen.fill((0, 0, 0))
        if is_blue:
            color = (0, 128, 255)
        else:
            color = (255, 100, 0)
        game.draw.rect(screen, color, game.Rect(x, y, 60, 60))

        game.display.flip()
        clock.tick(60)
