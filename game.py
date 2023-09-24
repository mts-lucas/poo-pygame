import pygame

import consts


class Game:
    # metodo contrutor
    def __init__(self) -> None:
        # iniciando o pygame
        pygame.init()
        # criando tela
        self.screen = pygame.display.set_mode(
            (consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.start = True
