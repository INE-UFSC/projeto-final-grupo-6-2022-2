import pygame
from abc import ABC, abstractmethod

class AbstractInterface(ABC):
    def __init__(self, screen, file_background_image):
        self.screen = screen
        self.background = pygame.image.load(file_background_image)

    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def draw(self):
        pass
    
    
    
    
    