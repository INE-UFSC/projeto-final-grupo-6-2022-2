import pygame
import sys

from abstractInterface import AbstractInterface
from optionsInterface import OptionsInterface
from button import Button

class MenuInterface(AbstractInterface):
    def __init__(self):
        super().__init__(pygame.display.get_surface(), 'interfaces\menu_jogo.png')
        self.__buttons = pygame.sprite.Group(
            [Button(1030, 350, 'interfaces\Botoes\\botao_start_hover.png',
                             'interfaces\Botoes\\botao_start.png', 
                             'interfaces\Botoes\\botao_start_pressed.png', 'start')],
            [Button(1030, 450, 'interfaces\Botoes\\botao_continue_hover.png',
                             'interfaces\Botoes\\botao_continue.png', 
                             'interfaces\Botoes\\botao_continue_pressed.png', 'continue')],
            [Button(1030, 550, 'interfaces\Botoes\\botao_options_hover.png',
                             'interfaces\Botoes\\botao_options.png', 
                             'interfaces\Botoes\\botao_options_pressed.png', 'options')],
            [Button(1030, 650, 'interfaces\Botoes\\botao_exit_hover.png',
                             'interfaces\Botoes\\botao_exit.png', 
                             'interfaces\Botoes\\botao_exit_pressed.png', 'exit')])

        self.__options = OptionsInterface()

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
                            self.__key = button.key
                            self.setButtonPressed()
            
            if self.getChangeInterface():
                if self.__key == 'options':
                    self.__options.start(clock)
                elif self.__key == 'exit':
                    pygame.quit()
                    sys.exit()
                elif self.__key == 'continue' or self.__key == 'start':
                    return self.__key
                
                self.setButtonPressed()

                
            self.cooldownBottonPressed()
            self.draw()
            pygame.display.flip()
    
    def draw(self):
        self.__buttons.update()
        self.getScreen().fill((0,0,0))
        self.getScreen().blit(self.getBackground(), ((1280-self.getBackground().get_rect()[2])//2,0))
        self.__buttons.draw(self.getScreen())

pygame.init()
window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
tela = MenuInterface()
tela.start(clock)