import pygame, sys
from settings import *
from level import Level
from interfaces.controlsInterface import ControlsInterface
from hud import Hud

class Game:
    def __init__(self):
        # Configuração inicial
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.clock = pygame.time.Clock()
        self.controles = ControlsInterface()
        self.level = Level()
        self.hud = Hud()

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.clock.tick(FPS)
            self.screen.fill((0, 0, 0))
            self.level.run()
            self.controles.draw()
            # self.hud.update()
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()
