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
        self.__nextInterface = None
        self.__running = False
        self.key = ''
        
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.key = self.__actualInterface.run()

            if self.key != None:
                if self.key == 'exit':
                    pygame.quit()
                    sys.exit()
                self.__nextInterface, self.__running = self.__interfaceController.nextInterface(self.key, self.__running)
                self.__actualInterface = self.__nextInterface
            self.clock.tick(FPS)             
            pygame.display.flip()
