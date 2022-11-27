import pygame, sys
from settings import *
from level import Level
from interfaces.controlsInterface import ControlsInterface
from interfaces.pauseInterface import PauseInterface
from hud import Hud

class Game:
    def __init__(self):
        # Configuração inicial
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.clock = pygame.time.Clock()
        self.pause = PauseInterface()
        self.controles = ControlsInterface()
        self.level = Level()
        self.hud = Hud()

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    key = self.pause.start(self.clock)
                    
                    if key == 'restart':
                        self.level = Level()
                
            self.clock.tick(FPS)
            self.screen.fill((0, 0, 0))
            self.level.run()
            self.controles.draw()
            # self.hud.update()
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()
