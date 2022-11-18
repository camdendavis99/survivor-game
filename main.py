import pygame


screen = pygame.display.set_mode([1080, 720])


def main():
    pygame.init()

    running = True
    while running:

        # Check if user closes window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == '__main__':
    main()
