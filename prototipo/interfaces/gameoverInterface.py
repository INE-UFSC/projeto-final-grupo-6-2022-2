import pygame

from interfaces.abstractInterface import AbstractInterface
from interfaces.button import Button

class GameOverInterface(AbstractInterface):
    def __init__(self):
        buttons = pygame.sprite.Group(
            [Button(1030, 350, 'interfaces\Botoes\\botao_restart_hover.png',
                             'interfaces\Botoes\\botao_restart.png', 
                             'interfaces\Botoes\\botao_restart_pressed.png', 'restart')],
            [Button(1030, 450, 'interfaces\Botoes\\botao_mainmenu_hover.png',
                             'interfaces\Botoes\\botao_mainmenu.png', 
                             'interfaces\Botoes\\botao_mainmenu_pressed.png', 'mainmenu')])
        
        super().__init__(pygame.display.get_surface(), 'interfaces\\telaMorte.png', buttons)

    def update(self):
        if self.getChangeInterface():
            return self.getKey()

    def draw(self):
        self.getButtons().update()
        self.getScreen().fill((0,0,0))
        self.getScreen().blit(self.getBackground(), ((1280-self.getBackground().get_rect()[2])//2,0))
        self.getButtons().draw(self.getScreen())
