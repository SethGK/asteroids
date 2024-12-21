import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, velocity, radius=SHOT_RADIUS):
        super().__init__(x, y, radius)  
        self.velocity = velocity  

    def draw(self, screen):
        white = (255, 255, 255)
        center = (self.position.x, self.position.y)  
        pygame.draw.circle(screen, white, center, self.radius)  

    def update(self, dt):
        self.position += self.velocity * dt  
