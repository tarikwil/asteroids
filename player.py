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
    
    def rotate(self, dt):
        self.rotation += const.PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_UP]:
            self.move(dt)
    
    def move(self, dt):
        self.position += pygame.Vector2(0, 1).rotate(self.rotation) * const.PLAYER_SPEED * dt