"""First attempt at pygame library use."""
import pygame as PG

def main():
    PG.init()

    # Setting screen size
    screen = PG.display.set_mode((240, 180))

    # Define basic running condition
    running = True

    while running:
        # Code follows event handling specific to pygame
        for event in PG.event.get():
            # Only do something if event is type QUIT like hitting window X button
            if event.type == PG.QUIT:
                # Exit game
                running = False

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
