import pygame

import consts


class Game:
    def __init__(self):
        # iniciando o pygame
        pygame.init()
        # criando tela
        self.screen = pygame.display.set_mode(
            (consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
        pygame.display.set_caption(consts.TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

    def game_events(self):
        # retorna todos os objetos do tipo event
        for event in pygame.event.get():
            # acessa o atributo type do objeto event
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):
        while self.running:
            # o metodo tick define os FPS do jogo
            self.clock.tick(consts.FPS)
            self.game_events()
