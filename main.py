import pygame
import constants as const
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    x = const.SCREEN_WIDTH / 2
    y = const.SCREEN_HEIGHT / 2
    p1 = Player(x, y)
    AsteroidField() 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for obj in updatable:    
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.is_colliding(p1):
                print("Game over!")
                exit()
                
        for obj in drawable:
            if isinstance(obj, Shot):
                obj.draw(screen, p1)
            else:
                obj.draw(screen)
            
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()