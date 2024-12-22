import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        white = (255,255,255)
        center = self.position.x,self.position.y
        pygame.draw.circle(screen, white,center,self.radius,2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            a1_vector = pygame.math.Vector2.rotate(self.velocity, random_angle)
            a2_vector = pygame.math.Vector2.rotate(self.velocity, -random_angle)
            
            a1_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            a2_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            a1_new_asteroid.velocity = a1_vector * 1.2
            a2_new_asteroid.velocity = a2_vector *1.2
            






         