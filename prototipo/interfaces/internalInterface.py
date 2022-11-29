import pygame, sys

from interfaces.abstractInterface import AbstractInterface
from abc import ABC, abstractmethod

class InternalInterface(AbstractInterface, ABC):
    def __init__(self, screen, file_background_image, buttons):
        super().__init__(screen, file_background_image, buttons)
        self.__clock = pygame.time.Clock()

    def run(self):
        run = True
        while run:
            self.draw()
            self.__clock.tick(60)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.getButtons():
                        if event.button == 1 and button.colliding():
                            self.setKey(button.key)
                            self.setButtonPressed()
            
            key = self.update()
            if key != None:
                self.setKey(None)
                return key
            
            
            self.cooldownBottonPressed()
            
            pygame.display.flip()
    
    @abstractmethod
    def draw(self):
        pass

    