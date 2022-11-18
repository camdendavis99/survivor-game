import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((80, 80, 200))
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys, screen_size):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_size[0]:
            self.rect.right = screen_size[0]
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_size[1]:
            self.rect.bottom = screen_size[1]
