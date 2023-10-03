import pygame

import consts


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = pygame.image.load("sprites/pipe.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 0
        self.speed = consts.PIPE_SPEED

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
