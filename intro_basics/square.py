"""Creating box with square that changes color.  

Link can be tutorial link can be found at: https://nerdparadise.com/programming/pygame/part1
"""
import pygame as PG


PG.init()
screen = PG.display.set_mode((800,300))
done = False
is_blue = True

while not done:
    for event in PG.event.get():
        if event.type == PG.QUIT:
            done = True
        
        # if event.type == PG.KEYDOWN and event.key == PG.K_SPACE:
        #     is_blue = not is_blue
        
        if event.type == PG.KEYDOWN and event.key == PG.K_SPACE:
            is_blue = not is_blue
    
        if is_blue:
            color = (0, 128, 255)
        else:
            color = (255, 100, 0)

    # Creating surface image with first element being color and second element being size
    # PG.draw.rect(screen, (0, 128, 255), PG.Rect(30, 30, 60, 60))  updating set color to color variable
    PG.draw.rect(screen, color, PG.Rect(30,30,60,60))

    PG.display.flip()
