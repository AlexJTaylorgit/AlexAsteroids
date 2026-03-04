import pygame
from logger import log_state,log_event
from constants import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField
from shot import *
import sys

def main():
    pygame.init()
    print("Starting Asteroids with pygame version: 2.6")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    asteroidField = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 0)
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #This line creates our Screen
    iteration_count = 1 #This is a dummy number for my infinite loop (line below)
    while iteration_count > 0:
        dt = clock.tick(60) / 1000 #Measures the time between clock ticks on the screen
        log_state()
        screen.fill("black")
        updatable.update(dt)
        for i in asteroids:
            if i.collides_with(player) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for i in asteroids:
            for s in shots:
                if i.collides_with(s) == True:
                    log_event("asteroid_shot")
                    pygame.sprite.Sprite.kill(s)
                    i.split()
        for i in drawable:
            i.draw(screen)
        pygame.display.flip() #Refreshes the Window 

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #so I can manually close the window without ctrl-C in the terminal
                return

            pass



if __name__ == "__main__":
    main()
