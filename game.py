import pygame

import consts
from plane import Plane


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

        # Inicialização de grupos de sprites
        self.all_sprites = pygame.sprite.Group()
        self.plane = Plane()
        self.all_sprites.add(self.plane)

    def game_events(self):

        # retorna todos os objetos do tipo event
        for event in pygame.event.get():
            # acessa o atributo type do objeto event
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.plane.flap()

    def run(self):
        while self.running:
            # o metodo tick define os FPS do jogo
            self.clock.tick(consts.FPS)
            self.game_events()
            # desenha as imagens na tela
            self.all_sprites.draw(self.screen)
            # chama o metodo update das classes
            self.all_sprites.update()
            pygame.display.flip()
            # sem isso a posicao anterior dos desenhos continua na tela
            self.screen.fill(consts.BLACK)
