import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):   
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        """if self.position.x > pygame.display.get_surface().get_width():
            self.position.x = 0
        if self.position.x < 0:
            self.position.x =  pygame.display.get_surface().get_width()
        if self.position.y >  pygame.display.get_surface().get_height():
            self.position.y = 0
        if self.position.y < 0:
            self.position.y =  pygame.display.get_surface().get_height()"""
        # above wraps asteroid movement for any display size

        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(rand_angle) * 1.2
        new_velocity2 = self.velocity.rotate(-rand_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid(self.position.x, self.position.y, new_radius).velocity = new_velocity1
        Asteroid(self.position.x, self.position.y, new_radius).velocity = new_velocity2