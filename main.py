import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


screen = pygame.display.set_mode([1080, 720])


def main():
    pygame.init()

    running = True
    while running:

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((128, 200, 128))
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
