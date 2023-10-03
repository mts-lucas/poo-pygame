import pygame

import consts


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("sprites/pipe.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = consts.PIPE_SPEED

    def update(self):
        # a cada momento atualizada a posicao
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
