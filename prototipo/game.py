import pygame, sys

from settings import WIDTH, HEIGTH, FPS
from screenController import ScreenController


class Game:
    def __init__(self):
        icone_do_jogo = pygame.image.load('interfaces/icone.png')
        pygame.display.set_caption('Flashlight')
        pygame.display.set_icon(icone_do_jogo)
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.clock = pygame.time.Clock()
        self.__screen_controller = ScreenController()
        self.__actualScreen = self.__screen_controller.firstScreen()
        
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            key = self.__actualScreen.run()
            
            if key != None:
                self.__actualScreen = self.__screen_controller.nextScreen(key, self.__actualScreen)
            
            self.clock.tick(FPS)
            pygame.display.flip()
