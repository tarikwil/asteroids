import pygame
import constants as const
import player

def main():
    pygame.init()
    screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT)) #add this for resize: pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    x = const.SCREEN_WIDTH / 2
    y = const.SCREEN_HEIGHT / 2
    p1 = player.Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(pygame.Color("black"))
        p1.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()