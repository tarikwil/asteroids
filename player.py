import pygame
import circleshape 
import constants as const

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, const.PLAYER_RADIUS)
        self.rotation = 0
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        const = self.position - forward * self.radius + right
        return [a, b, const]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, pygame.Color("white"), self.triangle(), 2)