import pygame

class ControlsInterface:
    def __init__(self):
        imgControle = pygame.image.load('interfaces\\telaControles.png')
        self.__rect = imgControle.get_rect()
        self.__active = False
        self.__image = pygame.Surface((self.__rect[2], 720))
        self.__image.fill((7,7,7))
        self.__image.blit(imgControle, (0, (720 - self.__rect[3])/2))
    
    def setActive(self):
        self.__active = not self.__active
    
    def draw(self, screen):
        if self.__active:

            screen.blit(self.__image, (1280 - self.__rect[2], 0))