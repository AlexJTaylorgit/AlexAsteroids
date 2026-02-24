import pygame
from logger import log_state
from constants import *
def main():
    pygame.init()
    print("Starting Asteroids with pygame version: 2.6")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #This line creates our Screen
    iteration_count = 1 #This is a dummy number for my infinite loop (line below)
    while iteration_count > 0:
        log_state()
        screen.fill("black")
        pygame.display.flip() #Refreshes the Window
        dt = clock.tick(60) / 1000 #Mesaures the time between refreshes of the screen

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #so I can manually close the window without ctrl-C in the terminal
                return

            pass




if __name__ == "__main__":
    main()
