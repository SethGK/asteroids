import pygame
import sys
pygame.init()

from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot

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
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)
    Player.containers = (updateable, drawable)
    Shot.containers = (shots,)

    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    
    dt = clock.tick(60)/10000
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        player.update(dt, shots) 

        black = (0,0,0)
        screen.fill(black)
        
        for i in updateable:
            if isinstance(i, Player):
                i.update(dt, shots)  
            else:
                i.update(dt) 
        
        for j in drawable:
            j.draw(screen)  

        for k in asteroids:
            if k.collisions(player):
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if k.collisions(shot):
                    k.kill()
                    shot.kill()
                    
        for shot in shots:
            shot.update(dt)
            shot.draw(screen)  


        pygame.display.flip()


if __name__ == "__main__":
    main()
