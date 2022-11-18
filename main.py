import pygame
from player import *
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
    player = Player()
    running = True

    while running:

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update player position
        pressed_keys = pygame.key.get_pressed()
        if True in pressed_keys:
            print("key pressed")
        player.update(pressed_keys)

        screen.fill((128, 200, 128))
        screen.blit(player.surf, player.rect)
        print(player.rect)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
