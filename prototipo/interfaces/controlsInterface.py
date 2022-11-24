import pygame

class ControlsInterface:
    def __init__(self):
        imgControle = pygame.image.load('interfaces\\telaControles.png')
        self.__screen = pygame.display.get_surface()
        self.__rect = imgControle.get_rect()
        self.__active = False
        self.__image = pygame.Surface((self.__rect[2], self.__screen.get_height()))
        self.__image.fill((7,7,7))
        self.__image.blit(imgControle, (0, (self.__screen.get_height() - self.__rect[3])/2))
    
    def setActive(self):
        self.__active = not self.__active
    
    def draw(self):
        if self.__active:

            self.__screen.blit(self.__image, (self.__screen.get_width() - self.__rect[2], 0))