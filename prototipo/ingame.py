import pygame
from settings import *
from level import Level



class InGame:
    def __init__(self, newgame):
        # Configuração inicial
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.level = Level()
        
        if not newgame:
            self.level.load()
        

    def run(self):
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            return 'pause'
        if self.level.getPlayerDead():
            return 'morreu'
        
        self.screen.fill((0, 0, 0))
        self.level.run()
        
    def draw(self):
        pass

        
        

