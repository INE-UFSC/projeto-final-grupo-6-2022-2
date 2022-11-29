import pygame

from interfaces.abstractInterface import AbstractInterface
from abc import ABC, abstractmethod

class ExternalInterface(AbstractInterface, ABC):
    def __init__(self, screen, file_background_image, buttons):
        super().__init__(screen, file_background_image, buttons)
    
    def run(self):
        self.draw()
        if pygame.mouse.get_pressed(num_buttons=3)[0]:
            for button in self.getButtons():
                if button.colliding():
                    self.setKey(button.key)
                    self.setButtonPressed()
            
        key = self.update()
        if key != None:
            self.setKey(None)
            return key
        
        
        self.cooldownBottonPressed()
    
    @abstractmethod
    def draw(self):
        pass

    
        
    