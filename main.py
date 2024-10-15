import pygame
import constants as const
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT)) #add this for resize: pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    asteroids = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = updatables

    x = const.SCREEN_WIDTH / 2
    y = const.SCREEN_HEIGHT / 2
    p1 = Player(x, y)
    AsteroidField() 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(pygame.Color("black"))
        for updateable in updatables:    
            updateable.update(dt)
        for asteroid in asteroids:
            if asteroid.is_colliding(p1):
                print("Game over!")
                exit()
        for drawable in drawables:
            drawable.draw(screen)
            
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()