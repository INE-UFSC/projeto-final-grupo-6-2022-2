import pygame
from settings import *
from level import Level



class InGame:
    def __init__(self):
        # Configuração inicial
        self.screen = pygame.display.get_surface()
        self.level = Level()
        
    def loadgame(self):
        self.level.load()
        

    def run(self):
        self.screen.fill((0, 0, 0))
        self.level.run()
        
        if self.level.getPlayerDead():
            return 'morreu'
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            return 'pause'
