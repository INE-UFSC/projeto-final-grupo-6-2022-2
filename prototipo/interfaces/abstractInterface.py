import pygame
from abc import ABC, abstractmethod

class AbstractInterface(ABC):
    def __init__(self, screen, file_background_image):
        self.__screen = screen
        self.__background = pygame.image.load(file_background_image)

    def getScreen(self):
        return self.__screen
    
    def getBackground(self):
        return self.__background
    
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def draw(self):
        pass
    
    
    
    
    