import pygame
import sys

from main import Game
from interfaces.abstractInterface import AbstractInterface
from interfaces.optionsInterface import OptionsInterface
from interfaces.controlsInterface import ControlsInterface
from interfaces.button import Button

class MenuInterface(AbstractInterface):
    def __init__(self):
        buttons = pygame.sprite.Group(
            [Button(1030, 250, 'interfaces\Botoes\\botao_start_hover.png',
                             'interfaces\Botoes\\botao_start.png', 
                             'interfaces\Botoes\\botao_start_pressed.png', 'start')],
            [Button(1030, 350, 'interfaces\Botoes\\botao_continue_hover.png',
                             'interfaces\Botoes\\botao_continue.png', 
                             'interfaces\Botoes\\botao_continue_pressed.png', 'continue')],
            [Button(1030, 450, 'interfaces\Botoes\\botao_options_hover.png',
                             'interfaces\Botoes\\botao_options.png', 
                             'interfaces\Botoes\\botao_options_pressed.png', 'options')],
            [Button(1030, 550, 'interfaces\Botoes\\botao_controls_hover.png',
                             'interfaces\Botoes\\botao_controls.png', 
                             'interfaces\Botoes\\botao_controls_pressed.png', 'controls')],
            [Button(1030, 650, 'interfaces\Botoes\\botao_exit_hover.png',
                             'interfaces\Botoes\\botao_exit.png', 
                             'interfaces\Botoes\\botao_exit_pressed.png', 'exit')])
        
        super().__init__(pygame.display.get_surface(), 'interfaces\menu_jogo.png', buttons)
        self.__options = OptionsInterface()
        self.__controls = ControlsInterface()

    def update(self):
        if self.getChangeInterface():
            key = self.getKey()
            if key == 'options':
                self.__options.start()
            elif key == 'exit':
                pygame.quit()
                sys.exit()
            elif key == 'controls':
                self.__controls.start()
            elif key == 'continue' or key == 'start':
                return key
                
            self.setButtonPressed()

    def draw(self):
        self.getButtons().update()
        self.getScreen().fill((0,0,0))
        self.getScreen().blit(self.getBackground(), ((1280-self.getBackground().get_rect()[2])//2,0))
        self.getButtons().draw(self.getScreen())
