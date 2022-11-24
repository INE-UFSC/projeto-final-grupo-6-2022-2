import pygame
import pygame_widgets

import sys
from pygame_widgets.slider import Slider
from abstractInterface import AbstractInterface
from button import Button

class OptionsInterface(AbstractInterface):
    def __init__(self):
        super().__init__(pygame.display.get_surface(), 'interfaces\menu_jogo.png')
        self.__buttons = pygame.sprite.Group([Button(150, 50, 'interfaces\Botoes\\botao_mainmenu_pressed.png', 
                                                              'interfaces\Botoes\\botao_mainmenu_pressed.png',
                                                              'interfaces\Botoes\\botao_mainmenu_pressed.png', 'voltar')])
        self.__slider = Slider(self.getScreen(), 500, 600, 500, 40, colour = (225, 215, 208), handleColour = (132, 116, 110))
        
    def start(self, clock):
        run = True
        while run:
            clock.tick(60)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.__buttons:
                        if event.button == 1 and button.colliding():
                            print('voltar para janela anterior')
                            return
            
            pygame_widgets.update(events)
            self.draw()
            pygame.display.flip()
    
    def draw(self):
        self.__buttons.update()
        self.getScreen().fill((0,0,0))
        self.getScreen().blit(self.getBackground(), ((1280-self.getBackground().get_rect()[2])//2,0))
        self.__buttons.draw(self.getScreen())
        self.__slider.draw()