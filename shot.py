import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen, p1):
        front_of_ship = self.position + pygame.Vector2(0, 1).rotate(p1.rotation) * PLAYER_RADIUS
        pygame.draw.circle(screen, "white", front_of_ship, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt