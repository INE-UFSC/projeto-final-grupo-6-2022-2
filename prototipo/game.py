import pygame, sys

from settings import WIDTH, HEIGTH, FPS
from screenController import ScreenController


class Game:
    def __init__(self):
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
                if key == 'exit':
                    pygame.quit()
                    sys.exit()
                self.__actualScreen = self.__screen_controller.nextScreen(key, self.__actualScreen)
            
            self.clock.tick(FPS)
            pygame.display.flip()
