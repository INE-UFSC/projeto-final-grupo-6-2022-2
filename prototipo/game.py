import pygame, sys

from settings import WIDTH, HEIGTH, FPS
from interfaceController import InterfaceController


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.clock = pygame.time.Clock()
        self.__interfaceController = InterfaceController()
        self.__actualInterface = self.__interfaceController.firstInterface()
        self.__running = False
        
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            key = self.__actualInterface.run()
            
            if key != None:
                if key == 'exit':
                    pygame.quit()
                    sys.exit()
                self.__actualInterface, self.__running = self.__interfaceController.nextInterface(key, self.__running)
            
            self.clock.tick(FPS)
            pygame.display.flip()
