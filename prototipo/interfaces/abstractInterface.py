import pygame
from abc import ABC, abstractmethod

class AbstractInterface(ABC):
    def __init__(self, screen, file_background_image):
        self.__screen = screen
        self.__background = pygame.image.load(file_background_image)
        self.__pressed_time = 60
        self.__button_pressed = False
        self.__change_interface = False

    def setButtonPressed(self):
        self.__button_pressed = not self.__button_pressed
    
    def getScreen(self):
        return self.__screen
    
    def getBackground(self):
        return self.__background
    
    def getChangeInterface(self):
        return self.__change_interface
    
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def draw(self):
        pass
    
    def cooldownBottonPressed(self):
        current_time = pygame.time.get_ticks()
        if self.__button_pressed:
            if current_time - self.__pressed_time > self.__pressed_time:
                self.__change_interface = True
        else:
            self.__change_interface = False
    
    
    
    
    