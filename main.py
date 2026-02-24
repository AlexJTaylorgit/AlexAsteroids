import pygame
from logger import log_state
from constants import *
def main():
    pygame.init()
    print("Starting Asteroids with pygame version: 2.6")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    iteration_count = 1
    while iteration_count > 0:
        log_state()
        for event in pygame.event.get():
            screen.fill("black")
            pygame.display.flip()
            if event.type == pygame.QUIT:
                return

            pass




if __name__ == "__main__":
    main()
