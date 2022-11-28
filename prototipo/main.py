import pygame, sys
from settings import *
from level import Level
from interfaces.pauseInterface import PauseInterface

class Game:
    def __init__(self):
        # Configuração inicial
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.clock = pygame.time.Clock()
        self.pause = PauseInterface()
        self.level = Level()

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    key = self.pause.start()
                    
                    if key == 'restart':
                        self.level = Level()
                    
                    if key == 'mainmenu':
                        return key
                
            self.clock.tick(FPS)
            self.screen.fill((0, 0, 0))
            self.level.run()
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()
