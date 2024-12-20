import pygame
import sys
pygame.init()

from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
dt = 0

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)
    Player.containers = (updateable, drawable)

    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    
    dt = clock.tick(60)/1000
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        black = (0,0,0)
        screen.fill(black)
        
        for i in updateable:
            i.update(dt)
        
        for j in drawable:
            j.draw(screen)

        for k in asteroids:
            if k.collisions(player):
                print("Game Over!")
                sys.exit()
        
        
        pygame.display.flip()


if __name__ == "__main__":
    main()