import pygame

import consts


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((consts.SCREEN_WIDTH, 20))
        self.image.fill(consts.BROWN)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = consts.SCREEN_HEIGHT - 20
